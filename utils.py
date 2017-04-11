# -*- coding: utf-8 -*-

import os.path
import sys 

path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)

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

    
