# import smtplib

# sender = 'ta4ckpih@gmail.com'
# receivers = ['serdiuk.o.e@gmail.com']

# message = """From: From Person <ta4ckpih@gmail.com>
# To: To Person <serdiuk.o.e@gmail.com>
# Subject: SMTP e-mail test

# This is a test e-mail message.
# """


# smtplib.SMTP('mail.google.com', 25)

# try:
# 	# smtpObj = smtplib.SMTP('localhost')
# 	smtpObj.sendmail(sender, receivers, message)         
# 	print "Successfully sent email"
# except Exception:
# 	print "Error: unable to send email"

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'me@mail.com'
msg['To'] = 'you@mail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('me@mail.com', 'password')

mailserver.sendmail(msg['From'], msg['To'],msg.as_string())

mailserver.quit()