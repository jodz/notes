# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 23:50:51 2017

@author: LiuWeipeng
"""

import smtplib
from email.mime.text import MIMEText

# 收件人列表
mail_namelist = ["569721942@qq.com"]
# 发送方信息
mail_user = "13330330435@qq.com"
#口令
mail_pass = "dttedbhptdngdfdb"

#发送邮件
#title：标题
#conen：内容
def send_qq_email(title,conen):
    try:
        msg = MIMEText(str(conen))
        #设置标题
        msg["Subject"] = title
        # 发件邮箱
        msg["From"] = mail_user
        #收件邮箱
        msg["To"] = ";".join(mail_namelist)
        # 设置服务器、端口
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        #登录邮箱
        s.login(mail_user, mail_pass)
        # 发送邮件
        s.sendmail(mail_user, mail_namelist, msg.as_string())
        s.quit()
        print("邮件发送成功!")
        return True
    except smtplib.SMTPException:
        print("邮件发送失败！")
        return False

send_qq_email("标题","内容")