#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def sendmail(rec_list,filename):
    sender = '490021209@qq.com'
    receivers =rec_list   # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Hackerl", 'utf-8')
    message['To'] =  Header("NetEasy 体验者", 'utf-8')
    subject = 'NetEasy App'
    message['Subject'] = Header(subject, 'utf-8')

    #邮件正文内容
    message.attach(MIMEText('这是最新版本App，旧版本已经无法使用，请下载安装新版本，如果有任何问题，回复邮件', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="NetEasy.app"'
    message.attach(att1)

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login('490021209@qq.com','password')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print '发送失败'
