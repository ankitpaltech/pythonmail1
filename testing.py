import smtplib
from email.mime.text import MIMEText

# connect with Google's servers
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# use username or email to log in
username = 'ankitpal4test@gmail.com'
password = 'sjrlxupsxhygccvc'

from_addr = 'ankitpal4test@gmail.com'
to_addrs = ['ankitpal4test@gmail.com']

# the email lib has a lot of templates
# for different message formats,
# on our case we will use MIMEText
# to send only text
message = MIMEText('Hello World this is ankit pal')
message['subject'] = 'Hello'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

# we'll connect using SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# to interact with the server, first we log in
# and then we send the message
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()