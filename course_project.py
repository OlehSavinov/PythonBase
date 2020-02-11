'''
Задание на курсовой проект
Разработать приложение “Адресная книга”
Реквизиты контакта:
● Фамилия - обязательно
● Имя - обязательно
● Отчество - опционально
● Почтовый адрес
● Список E-Mail в котором первый будет основным
● Список телефонов
● Список мессенджеров: пара значений - название (из предопределённого списка) и
аккаунт
Функциональность
1. Меню действий пользователя
a. Создать контакт
b. Вывести список контактов на экран в виде красивой таблицы.
c. Изменить контакт
d. Удалить контакт
e. Сохранить список контактов на диск
f. Поиск контакта по подстроке
i. по фамилии
ii. по имени
iii. по всем реквизитам
2. Прочитать список контактов с диска (если есть файл) при запуске программы
3. При выходе спрашивать о необходимости сохранения списка контактов в файл на
диск.
4. Вывести список контактов в текстовый файл (отчёт по всем реквизитам).
'''

from string import whitespace

class Contact:
    def __init__(self, surname, name, patronymic='НД', address=None, mail=None, tel=[], messenger={}):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.mail = mail
        self.tel = tel
        self.messenger = messenger
        global reg_id
        reg_id += 1
        self.id = reg_id

    def __str__(self):
        return f"{self.id}: {self.surname}, {self.name}, {self.patronymic}, {self.address}, {self.mail}, {self.tel}, {self.messenger}"

reg_id = 0


class AddressBook:
    name = 'Адресная книга'

    def __init__(self):
        self.contacts = []

    def append(self, contact):
        self.contacts.append(contact)

    def __str__(self):
        result = []
        for contact in self.contacts:
            result.append(str(contact))
        report_of_contacts = '\n'.join(result)
        return f"{report_of_contacts}"



c1 = Contact('Шевченко', 'Андрей', 'Викторович', 'ул. Хрещатик, 25, кв. 12', 'shevhcenko@gmail.com', '+380683582584', 'facebook: www.facebook.com/shevaa, telegram: andr_shev')
c2 = Contact('Петренко', 'Сергей', 'Петрович', 'ул. Мира, 10, кв. 2', 'petrenko@gmail.com, petr-ko@ukr.net', '+3809351348655', 'viber: petrenKO')
c3 = Contact('Короленко', 'Андрей', 'Владиславович', 'ул. Милютенко, 17, кв. 129', 'korolenko17@gmail.com', '+380972645123, +380635245548', 'telegram: kor_andr, whatsapp: kor_andr')


adress_book = AddressBook()
adress_book.append(c1)
adress_book.append(c2)
adress_book.append(c3)

inp = input('Для ввода котакта наберите "new": ')
if inp == 'new':
    surname = input('Введите фамилию: ')
    while not surname:
        surname = input('Фамилия - обязательное поле: ')
    name = input('Введите имя: ')
    while not name:
        name = input('Имя - обязательное поле: ')
    patronymic = input('Введите отчество: ')
    address = input('Введите адрес контакта: ')
    mail_osn = input('Введите основной электронный адрес контакта: ')
    while ' ' in mail_osn or not '@' in list(mail_osn)[1:-1]:
        if not mail_osn:
            break
        else:
            mail = input('Электронный адрес должен содержать "@" и не иметь пробелов: ')


    new_cont = Contact(surname, name, patronymic, address, mail)
    adress_book.append(new_cont)
print (adress_book)
