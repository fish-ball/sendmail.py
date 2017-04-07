#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from sys import stdin
from email.mime.text import MIMEText
import email

s = smtplib.SMTP_SSL('smtp.ym.163.com:465')
s.login('szshouko-fm@sz-nicchu.com','111111')

#f = open('mail.eml', 'wb')
#f.write(stdin.read())
#f.close()
#exit()

mail = email.message_from_string(stdin.read())
#print mail['from'], mail['to']


s.sendmail(mail['from'] or 'szshouko-fm@sz-nicchu.com', mail['to'], mail.as_string())
s.quit()

'''To: 57082212@qq.com
Subject: =?UTF-8?B?5L2g5aW9?=
X-PHP-Originating-Script: 1000:test.php
Content-type: text/plain; charset=utf-8;
From: Shenzhen JP <szshouko-fm@sz-nicchu.com>
This is a 特色他 伊妹儿'''
