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

    #from email.mime.text import MIMEText
    from random import random
    mail = open(os.path.join(
        settings.MAIL_DIR, 'draft', utils.generate_mail_file_name()
    ), 'w')
    #mail = email.message_from_string(stdin.read())
    mail.write(stdin.read())
    mail.close()

    exit()
    

#f = open('mail.eml', 'wb')
#f.write(stdin.read())
#f.close()
#exit()
#
#'''To: 57082212@qq.com
#Subject: =?UTF-8?B?5L2g5aW9?=
#X-PHP-Originating-Script: 1000:test.php
#Content-type: text/plain; charset=utf-8;
#From: Shenzhen JP <szshouko-fm@sz-nicchu.com>
#This is a 特色他 伊妹儿'''
