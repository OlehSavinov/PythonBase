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
    def __init__(self, surname, name, patronymic=None, address=None, mail=None, tel=None, messenger=None):
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
        return f"{self.id}; {self.surname} {self.name} {self.patronymic}; {self.address}; {self.mail}; {self.tel}; {self.messenger}"
reg_id = 0


class AddressBook:
    name = 'Адресная книга'

    def __init__(self):
        self.contacts = []

    def __str__(self):
        result = []
        for contact in self.contacts:
            result.append(str(contact))
        report_of_contacts = '\n'.join(result)
        return f"{report_of_contacts}"

    def append(self, contact):
        self.contacts.append(contact)

    def search_id(self, id):
        for cont in self.contacts:
            if cont.id == int(id):
                return cont

    def edit(self, cont_id, ind):
        cont = self.search_id(cont_id)
        if not cont:
            raise IndexError(f'Контакт с индексом {cont_id} не найден!')
        if ind == 'name':



c1 = Contact('Шевченко', 'Андрей', 'Викторович', 'ул. Хрещатик, 25, кв. 12', 'shevhcenko@gmail.com', '+380683582584', 'facebook: www.facebook.com/shevaa, telegram: andr_shev')
c2 = Contact('Петренко', 'Сергей', 'Петрович', 'ул. Мира, 10, кв. 2', 'petrenko@gmail.com, petr-ko@ukr.net', '+3809351348655', 'viber: petrenKO')
c3 = Contact('Короленко', 'Андрей', 'Владиславович', 'ул. Милютенко, 17, кв. 129', 'korolenko17@gmail.com', '+380972645123, +380635245548', 'telegram: kor_andr, whatsapp: kor_andr')

address_book = AddressBook()
address_book.append(c1)
address_book.append(c2)
address_book.append(c3)

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
    mail = ', '.join(mail)
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
    tel = ', '.join(tel)
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
    messenger = dict(messenger)
    new_cont = Contact(surname, name, patronymic, address, mail, tel, messenger)
    return new_cont

def view(adr):
    def max_len(l, n):
        l_res = []
        for i in range(len(l)):
            l_res.append(len(l[i][n]))
        return max(l_res)
    list_cont = adr.split('\n')
    s = []
    for i in range(len(list_cont)):
        s.append(list_cont[i].split('; '))
    l1 = []
    for i in range(len(s)):
        for j in range(5):
            l1.append(s[i][j])
    print('Сформированная таблица списка контактов:')
    print('| {0:^{1}} | {2:^{3}} | {4:^{5}} | {6:^{7}} | {8:^{9}} | {10:^{11}} |'.format('id', max_len(s, 0), 'ФИО', max_len(s, 1), 'Адрес', max_len(s, 2), 'E-mail', max_len(s, 3), 'Телефоны', max_len(s, 4), 'Мессенджеры', max_len(s, 5)))
    for j in range(len(s)):
        res = '| {0:<{1}}  | {2:<{3}} | {4:<{5}} | {6:<{7}} | {8:<{9}} | {10:<{11}} |'.format(s[j][0], max_len(s, 0), s[j][1], max_len(s, 1), s[j][2], max_len(s, 2), s[j][3], max_len(s, 3), s[j][4], max_len(s, 4), s[j][5], max_len(s, 5))
        print(res)

# def edit_cont(id):


inp = input('Для ввода контакта наберите "new": ')
if inp == 'new':
    new_cont = add_contact()
    address_book.append(new_cont)
    print('-'*60)
    print('Новый контакт "{0} {1}" с id "{2}" успешно добавлен'.format(new_cont.name, new_cont.surname, new_cont.id))
    print('-' * 60)
if inp == 'edit':
    ed = input('Какой из контактов Вы хотели бы изменить? Введите id контакта: ')
    print(address_book.edit(ed))

# print (adress_book)
# print(address_book)
# view(str(address_book))