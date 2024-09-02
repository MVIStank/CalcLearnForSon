import smtplib
import ssl


# TODO:
# Отправка статистики

class SmailS:
    def __init__(self, **kwargs):
        self.add_message = ""
        self.port = 465
        self.smtp_server = "smtp.yandex.ru"
        self.smtp_sender_mail = "volodiamiller@yandex.ru"
        self.receiver_mail = "volodiamiller@yandex.ru"
        self.password = "***"
        self.message = "Plan has been completed by Timofei: \n"
        print("Conctuctor has beeb worked")
        for key, value in kwargs.items():
            self.add_message += str(key) + " = " + str(value) + "\n"

    # print (**args)

    def send_email(self):
        print(" Попытка")
        self.message += self.add_message
        SSL_context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=SSL_context) as server:
            server.login(self.smtp_sender_mail, self.password)
            server.sendmail(self.smtp_sender_mail, self.receiver_mail, self.message)
        print(" Отправлено")
