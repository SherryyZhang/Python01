# -*- coding:utf-8 -*-
from email import encoders
form email.header import header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(),addr))

form_addr = input('Form: ')
password = input('Password: ')
to_addr = input('To :')
smtp_server = input('SMTP Server :')

msg = MIMEText('hello,send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python <%s>' % from_addr)
msg['To'] = _fomat_addr('administrator <%s>' % to_addr)
msg['Subject'] = Header('salut...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,[to_addr], msg.as_string())
server.qiut()
