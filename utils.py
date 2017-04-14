# -*- coding: utf-8 -*-

import os.path
import sys 

path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)

import re

import settings
import errno


def prepare_dir():
    from os import makedirs, chmod
    for name in ['draft', 'outbox', 'log', 'errorbox']:
        try:
            #print(os.path.join(settings.MAIL_DIR, name))
            dirname = os.path.join(settings.MAIL_DIR, name)
            makedirs(dirname)
            chmod(dirname, 0777)
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(dirname):
                pass
            else:
                print(e)


def generate_mail_file_name():
   from datetime import datetime
   from random import randint
   return datetime.now().strftime('%Y%m%d%H%M%S') + \
       '_{0:06d}'.format(randint(0,999999)) + '.eml'


def get_lock(process_name):
    import socket
    import sys
    """ http://stackoverflow.com/a/7758075/2544762 """
    get_lock._lock_socket = socket.socket(
        socket.AF_UNIX, socket.SOCK_DGRAM)

    try:
        get_lock._lock_socket.bind('\0' + process_name)
        print('Processing...')
    except socket.error:
        print('Another process running, process cancelled...')
        sys.exit()


def get_recipients(mail, type=''):
    data = dict(
        to=list(set([addr.strip() for addr in re.split(r'[,;]', mail['to'] or '') if '@' in addr])),
        cc=list(set([addr.strip() for addr in re.split(r'[,;]', mail['cc'] or '') if '@' in addr])),
        bcc=list(set([addr.strip() for addr in re.split(r'[,;]', mail['bcc'] or '') if '@' in addr])),
    )
    if type:
        return data.get(type, [])
    return list(set(data['to'] + data['cc'] + data['bcc']))


def split_mail(mail_content, batch_size):

    import email
    import re

    mail = email.message_from_string(mail_content)

    to = get_recipients(mail, 'to')
    cc = get_recipients(mail, 'cc')
    bcc = get_recipients(mail, 'bcc')
    receivers = list(set(to + cc + bcc))

    mails = []

    while receivers:
        batch_receivers = receivers[:batch_size]
        receivers[:batch_size] = []
        sub_mail = email.message_from_string(mail_content)

        del sub_mail['to']
        sub_mail['To'] = ', '.join([addr for addr in to if addr in batch_receivers])

        del sub_mail['cc']
        sub_mail['Cc'] = ', '.join([addr for addr in cc if addr in batch_receivers])

        del sub_mail['bcc']
        sub_mail['Bcc'] = ', '.join([addr for addr in bcc if addr in batch_receivers])

        mails.append(sub_mail.as_string())

    return mails

