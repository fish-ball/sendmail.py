#!/usr/bin/env sh

DIR=$(dirname $0)
TARGET=/usr/share/sendmail.py

#if [ -e /usr/sbin/sendmail ]; then
  #echo "ERROR: /usr/sbin/sendmail already exists, remove it and retry"
  #echo "You can run 'mv /usr/sbin/sendmail /usr/sbin/sendmail.bak' to move it"
#  exit 1 
#fi
mv -f /usr/sbin/sendmail /usr/sbin/sendmail.bak

mkdir -p $TARGET
cp $DIR/*.py $TARGET

ln -s $TARGET/sendmail.py /usr/sbin/sendmail
ln -s $TARGET/sendmaild.py /usr/sbin/sendmaild

./install.py

echo "Install successful"
echo "Please manually add * * * * * sendmaild to cronjob"
