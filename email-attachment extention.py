import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os # enter your email app passcode
to='nakkamanikanta1903@gmail.com'
From='nakkamanikanta1903@gmail.com'
#enter to whom you want to send
subject='mail with attachment'
text='sample test mail for attachment sending'
#body of mail
attach='shivaji.jpg'#give your attachment name
msg=MIMEMultipart()
msg['From']=From
msg['TO']=to
msg['subject']=subject
msg.attach(MIMEText(text))
#to load and encode the attachement
part=MIMEBase('application','octer-stream')
part.set_payload(open(attach,'rb').read())
encoders.encode_base64(part)
part.add_header('content-dispostion','attachment; filename="%s"' %os.path.basename(attach))
msg.attach(part)
#server connection starts...
mailserver=smtplib.SMTP('smtp.gmail.com',587)
mailserver.starttls()
mailserver.login(From,'qvhq nxzy lopy oygn')
#enter your gmail app pascode
mailserver.sendmail(From,to,msg.as_string())
print('done')
#close the connection
mailserver.close()
