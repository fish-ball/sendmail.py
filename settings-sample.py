# -*- coding: utf-8 -*-

# used by smtplib.SMTP_SSL() function
MAIL_SERVER='smtp.ym.163.com:465'

# smtp server login name
MAIL_LOGIN='user@example.com'

# smtp account password
MAIL_PASSWORD='mypassword'

# from mail address
MAIL_FROM='user@example.com'

# mail dir, the temp mail is stored in (outbox, draft, errorbox, log)
MAIL_DIR='/var/mail'

# recepients more than this number would split to multi mail
# http://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2cbaa9818223de0ad
BATCH_SIZE=20

# debug True/False
DEBUG=False

"""
1、网易企业邮箱：

网易163企业邮箱用户每15分钟发出邮件的总数上限:500封。
网易163企业邮箱用户当天发出邮件的总数上限:1000封。
网易163企业邮箱用户每15分钟发出邮件中收信人总人次上限:500人。
网易163企业邮箱用户当天发出邮件中收信人总人次上限:1000人。


IP同时连接数上限:5次。
IP每15分钟连接数上限:1500次。
IP每小时SMTP认证失败次数上限:300次。
IP每小时MAIL命令用户不存在比例上限(单位%):50%。
IP每小时RCPT命令用户不存在比例上限(单位%):50%。
IP当天连接数上限:50000次。
"""

# daily recepient quota
MAIL_QUOTA_DAY=1000

# send receipient quota in one batch, should be configured to a max allow send count in one cron run
MAIL_QUOTA_RUN=20
