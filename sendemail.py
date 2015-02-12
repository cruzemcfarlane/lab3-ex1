import smtplib

fromaddr = "info3180.cruze@gmail.com"
toaddr = "cruzemcfarlane@gmail.com"

message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""

messagetosend = message.format(
                               fromname,
                               fromaddr,
                               toname, 
                               toaddr, 
                               subject, 
                               msg
                               )
#Credentials (if needed)
username = 'info3180.cruze@gmail.com'
password = 'Naruto12?'

#The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.startls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, messagetosend)
server.quit()