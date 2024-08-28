import smtplib
import ssl
import datetime



class SmailS:
    def __init__(self):
        self.port = 465
        self.smtp_server = "smtp.yandex.ru"
        self.smtp_sender_mail = "volodiamiller@yandex.ru"
        self.receiver_mail = "volodiamiller@yandex.ru"
        self.password = "***"
        self.message = "Тимофей выполнил план!" + datetime.date.today().strftime("%B %d, %Y")
        print("Conctuctor has beeb worked")

    def send_email(self):
        print(" Попытка")
        SSL_context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server,self.port,context=SSL_context) as server:
            server.login(self.smtp_sender_mail,self.password)
            server.sendmail(self.smtp_sender_mail,self.receiver_mail,"test")
        print(" Отправлено")
