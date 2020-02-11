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
    def __init__(self, surname, name, patronymic='НД', address=None, mail=None, tel=[], messenger=[]):
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

def add_contact():
    surname = input('Введите фамилию: ')
    while not surname:
        surname = input('Фамилия - обязательное поле: ')
    name = input('Введите имя: ')
    while not name:
        name = input('Имя - обязательное поле: ')
    patronymic = input('Введите отчество: ')
    address = input('Введите адрес контакта: ')
    mail = []
    mail_i = input('Введите основной электронный адрес контакта: ')
    while mail_i:
        while ' ' in mail_i or not '@' in list(mail_i)[1:-1]:
            mail_i = input('Электронный адрес должен содержать "@" и не иметь пробелов: ')
            if not mail_i:
                break
        else:
            mail.append(mail_i)
            mail_i = input('Введите дополнительный электронный адрес контакта: ')
    tel = []
    tel_i = input('Введите номер телефона контакта (в формате "380669999999"): ')
    while tel_i:
        while not tel_i.isdigit() or len(tel_i) != 12:
            tel_i = input('Номер телефона ожидается в 12-значном числовом формате: ')
            if not mail_i:
                break
        else:
            tel.append('+' + tel_i)
            tel_i = input('Введите дополнительный номер телефона контакта: ')
    messenger = []
    mes_list = ['facebook', 'viber', 'telegram', 'whatsapp']
    mes_name = input('Введите название мессенджера {0}: '.format(mes_list))
    while mes_name:
        while mes_name not in mes_list:
            mes_name = input('Необходимо выбрать из представленного списка {0}: '.format(mes_list))
            if not mes_name:
                break
        else:
            mes_account = input('Введите адрес аккаунта в мессенджере {0}: '.format(mes_name))
            messenger.append((mes_name, mes_account))
            mes_name = input('Введите название дополнительного мессенджера {0}: '.format(mes_list))
    new_cont = Contact(surname, name, patronymic, address, mail, tel, messenger)
    return new_cont


inp = input('Для ввода котакта наберите "new": ')
if inp == 'new':
    new_cont = add_contact()
    adress_book.append(new_cont)
    print('-'*60)
    print('Новый контакт "{0} {1}" с id "{2}" успешно добавлен'.format(new_cont.name, new_cont.surname, new_cont.id))
    print('-' * 60)

print (adress_book)
