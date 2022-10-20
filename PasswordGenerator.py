from tkinter import Tk, Frame, Checkbutton, Entry, Button, messagebox, Label
from tkinter import BooleanVar, BOTH, StringVar
import random


class Example(Frame):
    string = ''
    def __init__(self):
        # Frame.__init__(self) #понять разницу между этим и этим, изначально было с super() --- super() позволяет вызывать функции данного класса в других классах, если его не использовать, то наследование из одного класса в другой не произойдёт
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Генератор паролей")
        self.pack(fill=BOTH, expand=True)
        self.boolean_button_digit_var = BooleanVar()
        self.boolean_button_lowercase_var = BooleanVar()
        self.boolean_button_uppercase_var = BooleanVar()
        self.boolean_button_sign_var = BooleanVar()

        #InputArea
        self.message = StringVar()
        message_entry = Entry(textvariable=self.message)
        message_entry.place(relx=.5, rely=.1, anchor="c")

        #CheckbuttonArea
        boolean_button_digit_var = Checkbutton(text="Числа", variable=self.boolean_button_digit_var,
                                               command=self.digit_boolean)
        boolean_button_digit_var.place(relx=.1, rely=.4, anchor="w")
        boolean_button_lowercase = Checkbutton(text="Строчные буквы", variable=self.boolean_button_lowercase_var,
                                               command=self.lowercase_boolean)
        boolean_button_lowercase.place(relx=.1, rely=.5, anchor="w")
        boolean_button_uppercase = Checkbutton(text="Заглавные буквы", variable=self.boolean_button_uppercase_var,
                                               command=self.uppercase_boolean)
        boolean_button_uppercase.place(relx=.1, rely=.6, anchor="w")
        boolean_button_sign = Checkbutton(text="Знаки", variable=self.boolean_button_sign_var,
                                          command=self.sign_boolean)
        boolean_button_sign.place(relx=.1, rely=.7, anchor="w")

        # ButtonArea
        start_button = Button(text="Сгенерировать пароль", command=self.password_generator)
        start_button.place(relx=.5, rely=.2, anchor="w")
        confirmation_button = Button(text="Подтвердить", command=self.attribute_processor)
        confirmation_button.place(relx=.1, rely=.2, anchor="w")
        refresh_settings = Button(text="Refresh", command=self.settings_refresher)
        refresh_settings.place(relx=.1, rely=.3, anchor="w")

    def settings_refresher(self):
        self.boolean_button_digit_var = BooleanVar()
        self.boolean_button_lowercase_var = BooleanVar()
        self.boolean_button_uppercase_var = BooleanVar()
        self.boolean_button_sign_var = BooleanVar()
        #EmptyString
        Example.string = ''
        #CheckbuttonArea
        boolean_button_digit_var = Checkbutton(text="Числа", variable=self.boolean_button_digit_var,
                                               command=self.digit_boolean)
        boolean_button_digit_var.place(relx=.1, rely=.4, anchor="w")

        boolean_button_lowercase = Checkbutton(text="Строчные буквы", variable=self.boolean_button_lowercase_var,
                                               command=self.lowercase_boolean)
        boolean_button_lowercase.place(relx=.1, rely=.5, anchor="w")

        boolean_button_uppercase = Checkbutton(text="Заглавные буквы", variable=self.boolean_button_uppercase_var,
                                               command=self.uppercase_boolean)
        boolean_button_uppercase.place(relx=.1, rely=.6, anchor="w")

        boolean_button_sign = Checkbutton(text="Знаки", variable=self.boolean_button_sign_var,
                                          command=self.sign_boolean)
        boolean_button_sign.place(relx=.1, rely=.7, anchor="w")

    def attribute_processor(self):
        self.val_message_entry = self.message.get()
        if self.val_message_entry == '':
            self.new_value = 0
        else:
            self.new_value = int(self.message.get())

    def password_generator(self):
        password = ''
        if Example.string != '' or self.new_value == 0:
            for x in range(self.new_value):  # Количество символов (self.new_value)
                password = password + random.choice(list(Example.string))  # выбранные символы, из которых будет составлен пароль
            messagebox.showinfo("пример ввода\вывода", "ваш пароль: " + password)
        else:
            messagebox.showinfo('', 'wwhdith 3islo')

    def digit_boolean(self):
        digit = '1234567890'
        if self.boolean_button_digit_var.get():
            Example.string += digit
            return Example.string
        else:
            return ''

    def lowercase_boolean(self):
        lowercase = 'abcdefghigklmnopqrstuvyxwz'
        if self.boolean_button_lowercase_var.get():
            Example.string += lowercase
            return Example.string
        else:
            return ''

    def uppercase_boolean(self):
        uppercase = 'ABCDEFGHIGKLMNOPQRSTUVYXWZ'
        if self.boolean_button_uppercase_var.get():
            Example.string += uppercase
            return Example.string
        else:
            return ''

    def sign_boolean(self):
        sign = '!#$%^&*[];:><'
        if self.boolean_button_sign_var.get():
            Example.string += sign
            return Example.string
        else:
            return ''


def main():
    root = Tk()
    root.geometry("300x250")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()