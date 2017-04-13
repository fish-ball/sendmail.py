# -*- coding: utf-8 -*-

# used by smtplib.SMTP_SSL() function
MAIL_SERVER='smtp.ym.163.com:465'

# smtp server login name
MAIL_LOGIN='user@example.com'

# smtp account password
MAIL_PASSWORD='mypassword'

# from mail address
MAIL_FROM='user@example.com'

# mail dir, the temp mail is stored in ($MAIL_DIR/outbox $MAIL_DIR/draft)
MAIL_DIR='/var/mail'

# recepients more than this number would split to multi mail
# http://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2cbaa9818223de0ad
BATCH_SIZE=40

# debug True/False
DEBUG=False
