#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys

path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)

import settings
import utils

from sys import stdin

if __name__ == '__main__':

    utils.prepare_dir()

    # Split the mail by recepients and save to draft queue
    for mail_content in utils.split_mail(stdin.read(), settings.BATCH_SIZE or 20):
        mail = open(os.path.join(settings.MAIL_DIR, 'draft', utils.generate_mail_file_name()), 'w')
        mail.write(mail_content)
        mail.close()

    exit()
    
