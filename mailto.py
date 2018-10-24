#!/usr/bin/env python
# coding=utf8
import sys
import os
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

reload(sys)
sys.setdefaultencoding("utf-8")

mail_host = "smtp.163.com"  # 设置服务器
mail_user = "godspeed_ls"  # "tonygodspeed"    #用户名
mail_pass = "123!@#ZZZ"  # "wakinlsATtony163"   #口令
mail_postfix = "163.com"  # 发件箱的后缀


def send_mail(to_list, sub, content, attachment_file):
	me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"
	msg = MIMEMultipart()  # MIMEText(content,_subtype='plain',_charset='utf-8')
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	if len(content) > 0:
		msg.attach(MIMEText(content, _subtype="plain", _charset='utf-8'))

	if len(attachment_file) > 0 and os.path.exists(attachment_file):
		att = MIMEText(open(attachment_file, 'rb').read(), 'base64', 'utf-8')
		att["Content-Type"] = 'application/octet-stream'
		att["Content-Disposition"] = 'attachment; filename="@log.txt"'
		msg.attach(att)

	try:
		server = smtplib.SMTP()
		server.connect(mail_host)
		server.login(mail_user, mail_pass)
		server.sendmail(me, to_list, msg.as_string())
		server.close()
		return True
	except Exception, e:
		print str(e)
		return False


if __name__ == '__main__':
	if send_mail(mailto_list, "hello", "hello world！", 'E:\\@log.txt'):
		print "发送成功"
	else:
		print "发送失败"
