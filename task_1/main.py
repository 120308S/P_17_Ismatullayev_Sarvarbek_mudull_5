import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from celery import Celery

app = Celery('hello', broker='pyamqp://guest@localhost/')

@app.task
def emails_send():

    logging.basicConfig(filename="EMAIL.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    emails = """
       sarvarismatullayev7@gmail.com,
       sarvarismatullayev3@gmail.com,
       sarvarbekismatullayev0@gmail.com,
       ismatullayevsarvar36@.gmail.com
       """.split('\n')
    for i in emails:

        sender_email = "sarvarismatullayev7@gmail.com"
        sender_password = "ruumgybqddjbiqyh"
        receiver_email = i
        subject = "Muhammad"
        message = "Nima gap"


        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        try:
            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)
            text = msg.as_string()
            smtp_server.sendmail(sender_email, receiver_email, text)
            smtp_server.quit()
            logging.info("E-pochta muvaffaqiyatli yuborildi!")
        except Exception as e:
            logging.error(f"E-pochta yuborilmadi. Xatolik: {str(e)}")

emails_send()
