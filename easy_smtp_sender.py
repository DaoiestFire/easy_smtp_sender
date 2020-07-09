# -*- coding: utf-8 -*-
# This module is a simple smtp sender
# if you train you model in a remote machine
# and need to check the state of the model or The training results frequently,
# this module will help you by sending data (text,image,video) to you mailbox
# QQ-Email Has been supported

import smtplib
from smtplib import SMTPServerDisconnected
import os
import sys

from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class EasySmtpSender(object):
    def __init__(self, sender, password, receiver=None, msg_from=None, is_silent=True):
        super(EasySmtpSender, self).__init__()

        self.sender = sender
        self.password = password
        if receiver is not None:
            self.receiver = receiver
        else:
            self.receiver = sender
        self.msg_from = msg_from

        self.smtp_server = "smtp.qq.com"
        self.smtp_port = 465

        self.msg = MIMEMultipart('related')
        if self.msg_from is not None:
            self.msg['From'] = Header(self.msg_from, 'utf-8')
        else:
            self.msg['From'] = Header(self.sender, 'utf-8')
        self.msg['To'] = Header(self.receiver, 'utf-8')

        # attachment attribute
        self.content_type = 'application/octet-stream'
        self.main_type, self.sub_type = self.content_type.split('/', 1)

        # smtp server
        self.server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)

        # whether output successful information
        self.is_silent = is_silent

    def __del__(self):
        self.server.quit()

    def init_msg(self):
        self.msg = MIMEMultipart('related')
        if self.msg_from is not None:
            self.msg['From'] = Header(self.msg_from, 'utf-8')
        else:
            self.msg['From'] = Header(self.sender, 'utf-8')
        self.msg['To'] = Header(self.receiver, 'utf-8')

    def add_main_body_text(self, main_body_text):
        message = MIMEText(main_body_text, 'plain', 'utf-8')
        self.msg.attach(message)

    def add_attachment(self, path_to_file):
        with open(path_to_file, 'rb') as f:
            file_msg = MIMEBase(self.main_type, self.sub_type)
            file_msg.set_payload(f.read())
        encoders.encode_base64(file_msg)
        basename = os.path.basename(path_to_file)
        file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
        self.msg.attach(file_msg)

    def send_email(self, subject, main_body_text=None, attachment=None):
        self.init_msg()
        self.msg['Subject'] = Header(subject, 'utf-8')
        if main_body_text is not None:
            self.add_main_body_text(main_body_text)
        if attachment is not None:
            if isinstance(attachment, list):
                for file in attachment:
                    self.add_attachment(file)
            else:
                self.add_attachment(attachment)

        # send a e-mail
        try:
            self.server.connect(self.smtp_server)
            self.server.login(self.sender, self.password)
            self.server.sendmail(self.sender, [self.receiver], self.msg.as_string())
            if not self.is_silent:
                print('send e-mail successfully')
        except SMTPServerDisconnected:
            self.server.login(self.sender, self.password)
            self.server.sendmail(self.sender, [self.receiver], self.msg.as_string())
            if not self.is_silent:
                print('send e-mail successfully')
        except Exception:
            sys.stderr.write('fail to send e-mail')
