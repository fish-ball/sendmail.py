#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: 日志记录尚未完善

import os.path
import sys 

path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)

import smtplib
import email

import settings
import utils

#def get_recipients(addr_list_str):
#    return list(set(
#        [addr.strip() for addr in addr_list_str.split(',') if '@' in addr]
#    ))


if __name__ == '__main__':

    # Locks only one process can be running
    utils.get_lock('sendmaild')

    s = smtplib.SMTP_SSL(settings.MAIL_SERVER)

    if settings.DEBUG:
        s.set_debuglevel(1)

    draft_dir = os.path.join(settings.MAIL_DIR, 'draft')
    outbox_dir = os.path.join(settings.MAIL_DIR, 'outbox')
    errorbox_dir = os.path.join(settings.MAIL_DIR, 'errorbox')

    s.login(settings.MAIL_LOGIN, settings.MAIL_PASSWORD)

    for filename in os.listdir(draft_dir):

        if not filename.endswith('.eml'):
            continue

        draft_file = os.path.join(draft_dir, filename)
        outbox_file = os.path.join(outbox_dir, filename)
        errorbox_file = os.path.join(errorbox_dir, filename)
        mail_content = open(draft_file, 'r').read()

        mail = email.message_from_string(mail_content)
        os.unlink(draft_file)

        try:
            mail = email.message_from_string(mail_content)
            to = mail['to']
            if mail['cc']:
                to += ', ' + mail['cc']
            if mail['bcc']:
                to += ', ' + mail['bcc']
            to = list(set(
                [addr.strip() for addr in to.split(',') if '@' in addr]
            ))
            assert to, 'No valid recepients.'
            while to:
                batch = to[:settings.BATCH_SIZE]
                print('<<<<<<<<<<<< BATCH: %d' % len(batch))
                print(batch)
                to[:settings.BATCH_SIZE] = []
		s.sendmail(settings.MAIL_FROM, batch, mail.as_string())
            open(outbox_file, 'w').write(mail_content)
        except Exception as e:
            print('!!!!!!!!!!!!!!! <Exception> %s' % e)
            open(errorbox_file, 'w').write(mail_content)

    s.quit()
