import smtplib

fromaddr = "info3180.cruze@gmail.com"
toaddr = "cruze.mcfarlane@hotmail.com"

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""

fromname = "Cruze Martinez"
fromaddr = "info3180.cruze@gmail.com"
toname = "Cruze McFarlane"
toaddrs = "cruze.mcfarlane@hotmail.com"
subject = "Yea it works!"
msg = "Damn this is awesome"

messagetosend = message.format(
 fromname,
 fromaddr,
 toname,
 toaddr,
 subject,
 msg)

#Credentials (if needed)
username = 'info3180.cruze@gmail.com'
password = 'kxjfgocykwketvrw'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()