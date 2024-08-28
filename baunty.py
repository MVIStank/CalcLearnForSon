import random
import json
from tkinter import *
from datetime import date


class Block:

    def __init__(self, master):
        #self.lst = {"time": "0", "all_attempt": 0, "all_today": 0, "success_attempt": 0, "error_attempt": 0}
       # self.json_write()
        # загрузка результатов
        self.lst = self.json_load()
        self.prepare_json()

        # генерация двух чисел
        self.first_number, self.second_number = self.rand_a()
        self.sum_min = self.rand_sum_min()

        # чек. Был ли первый ответ
        self.check_first_answer = 1

        self.geometry = master.geometry("620x600")
        self.welcome = master.title("Тимофей, давай учиться считать!")
        self.lab = Label(master, text="Посчитай, сколько получится?")
        # Фон фото
        self.image = PhotoImage (file="/home/vladimir/Downloads/t1.png")
        self.image_label = Label(master, image=self.image)

        self.ent = Entry(master, width=10)
        self.ent.insert(0,str(self.first_number) + " " + self.sum_min + " " + str(self.second_number))
        self.lab1 = Label(master,text="Твой ответ")
        self.but = Button(master, text='Проверить',command=self.action_button)
        self.gen_new_but = Button(master, text='Cгенерировать новое значение', command=self.gen_action_button)
        self.answer = Text(width=30, height=1)
        self.stats = Label(master,  text="Статистика:")
        self.all_attempt = Label(master,text="Всего примеров :  " + str(self.lst["all_attempt"]))
        self.all_today = Label(master, text="Примеров за сегодня :  " + str(self.lst["all_today"]))
        self.success_attempt = Label(master,text="Примеров решено успешно :  " + str(self.lst["success_attempt"]) + self.calculate_percent())
        self.error_attempt = Label(master, text="Примеров решено с ошибкой :  " + str(self.lst["error_attempt"]))
        self.cngt = Label(master)
        self.lab.pack()
        self.ent.pack()
        self.lab1.pack()
        self.answer.pack()
        self.but.pack()
        self.gen_new_but.pack()
        self.stats.place(x = 250, y=160)
        self.all_attempt.place(x=20, y=180)
        self.all_today.place(x=20, y=200)
        self.success_attempt.place(x=315, y=180)
        self.error_attempt.place(x=315, y=200)
        self.cngt.place(x=50, y=300)
        self.image_label.pack(pady=10)

    def rand_a(self):
        ls =[]
        number_a = random.randint(1, 10)
        number_b = random.randint(1, 10)
        if number_a >= number_b:
            ls =[number_a,number_b]
            return ls
        else:
            ls = [number_b, number_a]
            return ls

    def rand_sum_min(self):
        number = random.randint(0, 1)
        if number == 0:
            print(1)
            self.mode = 1
            return "+"
        else:
            print(0)
            self.mode = 0
            return "-"

#нажата кнопка "Проверить"
    def action_button(self):
        str = self.answer.get("1.0", END)
        try:
            self.tim_answer = int(str)
            if self.check_answer():
                self.lab1.config(text="Умничка! Верно!",bg= "green")
            else:
                self.lab1.config(text="Неверно", bg="yellow")
            if self.check_first_answer:
                self.set_count_attempt()
                self.json_write()
            self.check_first_answer = 0
            self.update_label()

        except ValueError:
            self.lab1.config(text=" Ответ должен быть ввиде числа!", bg="red")


    def check_answer(self):
        if self.mode:
            if self.tim_answer == self.first_number + self.second_number:
                return 1
            else:
                return 0
        else:
            if self.tim_answer == self.first_number - self.second_number:
                return 1
            else:
                return 0

    def gen_action_button(self):
        self.sum_min = self.rand_sum_min()
        self.first_number,self.second_number = self.rand_a()
        self.ent.delete(0, END)
        self.ent.insert(0, str(self.first_number) + " " + self.sum_min + " " + str(self.second_number))
        self.lab1.config(text="Твой ответ",bg="white")
        self.check_first_answer = 1

#### Работа с JSON ######
    def json_load(self):
      with open("/home/vladimir/Downloads/answer.json", "r") as file_stream:
        return json.load(file_stream)


    def json_write (self):
      with open("/home/vladimir/Downloads/answer.json", "w") as file_stream:
            json.dump(self.lst,file_stream)
            file_stream.write('\n')

    def prepare_json(self):
        current_date = date.today()
        current_date = current_date.strftime("%B %d, %Y")
        if self.lst["time"] != current_date:
            print(current_date)
            self.lst["all_today"] = 0
            self.lst["success_attempt"] = 0
            self.lst["error_attempt"] = 0
            self.lst["time"] = current_date
            self.json_write()


    def set_count_attempt (self):
        current_date = date.today()
        current_date = current_date.strftime("%B %d, %Y")
        if self.check_first_answer:
            self.lst["all_attempt"] += 1
            if self.lst["time"] == current_date:
                self.lst["all_today"] += 1
            if self.check_answer():
                self.lst["success_attempt"] += 1
            else:
                self.lst["error_attempt"] += 1


    def calculate_percent(self):
        try:
            a = round((self.lst["success_attempt"] / self.lst["all_today"]) * 100, 1)
        except ZeroDivisionError:
            a = 0
        return " (" + str(a) + " % )"

    def update_label(self):
        self.all_attempt.config(text="Всего примеров :  " + str(self.lst["all_attempt"]))
        self.all_today.config(text="Примеров за сегодня :  " + str(self.lst["all_today"]))
        self.success_attempt.config(text="Примеров решено успешно :  " + str(self.lst["success_attempt"]) + self.calculate_percent())
        self.error_attempt.config(text="Примеров решено с ошибкой :  " + str(self.lst["error_attempt"]))
        if self.lst["success_attempt"] > 20:
            self.cngt.config(text = " МОЛОДЕЦ! Ты решил дневную норму. Можно взять у родителей вкусняшку!:)", fg="blue")

root = Tk()

first_block = Block(root)


root.mainloop()
