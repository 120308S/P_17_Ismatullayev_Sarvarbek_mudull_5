import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "sarvarismatullayev7@gmail.com"
receiver_email = "sarvarismatullayev3@gmail.com"
password = ""


subject = "Salom"
body = "Nima gap"


smtp_server = "smtp.gmail.com"
smtp_port = 587


server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()


server.login(sender_email, password)


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))


server.sendmail(sender_email, receiver_email, message.as_string())


server.quit()

