#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
import unittest
import time,os


#==============定义发送邮件 =============

def send_mail(file_new):
    username = 'xbwu@dataman-inc.com'
    password = 'Wu123456'
    with open(file_new,'rb') as f:
        mail_body = f.read()
    #编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    #通过  模块构造的带附件的邮件如图
    msg = MIMEMultipart()
    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('Solar项目API测试', 'utf-8')
    msg.attach(text)
    
    #发送附件
    msg['Subject'] = Header('Solar项目API接口自动化测试报告', 'utf-8')
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="TestReport of Solar API.html"'
    msg.attach(msg_file)
    msg['from'] = 'xbwu@dataman-inc.com'
    msg1= ['xbwu@dataman-inc.com','2683904575@qq.com']
    print(msg1)
    smtp = smtplib.SMTP('smtp.exmail.qq.com', 25)
    smtp.connect('smtp.exmail.qq.com')
    smtp.login(username, password) 
    smtp.sendmail(msg['from'], msg1, msg.as_string())
    smtp.quit()
    print("邮件发送成功!")

#=====================发送测试报告==================

if __name__ == '__main__':
    test_dir = "D:\workspace\SRATV4\src"
    test_report = os.path.join("D:\\test_object", 'report')
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='Case*.py')
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = test_report + r'\Solar API TestResult-' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title="Solar项目API自动化测试报告",description='Solar项目API用例执行情况：')
    runner.run(discover)
    fp.close()
    send_mail(filename) 
    