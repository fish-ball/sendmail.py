#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys

path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)

import settings
import utils

import smtplib
import email
import re

from datetime import datetime

if __name__ == '__main__':

    # Locks only one process can be running
    utils.get_lock('sendmaild')

    s = smtplib.SMTP_SSL(settings.MAIL_SERVER)

    if settings.DEBUG:
        s.set_debuglevel(1)

    draft_dir = os.path.join(settings.MAIL_DIR, 'draft')
    outbox_dir = os.path.join(settings.MAIL_DIR, 'outbox')
    errorbox_dir = os.path.join(settings.MAIL_DIR, 'errorbox')

    log_dir = os.path.join(settings.MAIL_DIR, 'errorbox')
    log_file = os.path.join(settings.MAIL_DIR, 'log', datetime.now().strftime('%Y-%m-%d')+'.log')
    logger = open(log_file, 'a')
    logger.save()
    logger.close()
    

    s.login(settings.MAIL_LOGIN, settings.MAIL_PASSWORD)

    quota = settings.MAIL_QUOTA_RUN
    quota_day = settings.MAIL_QUOTA_DAY - sum([1 for line in open(log_file, 'r') if 'OK' in line])

    print('quota: ', quota)
    print('quota_day: ', quota_day)

    for filename in os.listdir(draft_dir):

        if not filename.endswith('.eml'):
            continue

        draft_file = os.path.join(draft_dir, filename)
        outbox_file = os.path.join(outbox_dir, filename)
        errorbox_file = os.path.join(errorbox_dir, filename)

        mail_content = open(draft_file, 'r').read()
        mail = email.message_from_string(mail_content)
        to = utils.get_recipients(mail)

        if len(to) > quota or len(to) > quota_day:
            break

        os.unlink(draft_file)

        logger = open(log_file, 'a')

        try:
            mail = email.message_from_string(mail_content)
            
            s.sendmail(settings.MAIL_FROM, to, mail.as_string())
            for addr in to:
                quota -= 1
                quota_day -= 1
                logger.write('[%s] OK   %s >> %s\n' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), filename, addr))
            open(outbox_file, 'w').write(mail_content)
        except Exception as e:
            print('!!!!!!!!!!!!!!! <Exception> %s' % e)
            for addr in to:
                logger.write('[%s] FAIL %s >> %s\n' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), filename, addr))
            open(errorbox_file, 'w').write(mail_content)
        
        logger.close()

    s.quit()
