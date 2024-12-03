import re

user_list = []

while True:
    user_data_list = []
    user_name = input("Введите имя пользователя или stop для завершения: ").strip().title()
    reg_name = re.compile(r'[A-Za-zА-Яа-я]+')
    while not bool(reg_name.fullmatch(user_name)):
        user_name = input(
            "Содержит неподходящие символы. Введите имя пользователя или stop для завершения: ").strip().title()
        if user_name == 'Stop':
            break
    if user_name == "Stop":
        break
    else:
        print("Имя принято")
        user_data_list.append(user_name)
    surname = input("Введите Фамилию пользователя или stop для завершения: ").strip().title()
    reg_surname = re.compile(r'[A-Za-zА-Яа-я]+')
    while not bool(reg_surname.fullmatch(surname)):
        surname = input(
            "Содержит неподходящие символы. Введите Фамилию пользователя или stop для завершения: ").strip().title()
        if surname == 'Stop':
            break
    if surname == "Stop":
        break
    else:
        print("Фамилия принята")
        user_data_list.append(surname)
    tel_number = input("Ввдите телефон в формате +***(**)******* или stop для завершения: ").strip().title()
    reg_tel_number = re.compile(r'\+\d{1,3}\(\d\d\)\d{7}$')
    while not bool(reg_tel_number.fullmatch(tel_number)):
        tel_number = input(
            "Не соответствует формату +***(**)*******. Ввдите телефон в формате +***(**)*******: или stop для завершения: ").strip().title()
        if tel_number == 'Stop':
            break
    if tel_number == "Stop":
        break
    else:
        print("Телефон принят")
        user_data_list.append(tel_number)
    yandex_name = input("Введите email на яндексеили stop для завершения или stop для завершения: ").strip()
    reg_2 = re.compile(r'[A-Za-z0-9._-]+@yandex\.ru$')
    while not bool(reg_2.fullmatch(yandex_name)):
        yandex_name = input(
            "Почта должна состоять из латинских букв или цифр и содержать @yandex.ru, введите ещё раз или stop для завершения: ").strip()
        if yandex_name == 'Stop':
            break
    if yandex_name == "Stop":
        break
    else:
        print("Почта принята")
        user_data_list.append(yandex_name)

    if user_list.count(user_data_list) < 1:
        user_list.append(user_data_list)
    else:
        print(f"{user_data_list} уже существует, введите другого пользователя ")

for i in range(len(user_list)):
    print(user_list[i])


