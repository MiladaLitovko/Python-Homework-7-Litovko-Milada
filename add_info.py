

def new_info():
    info_first_name = str(input('Введите фамилию: '))
    info_second_name = str(input('Введите имя: '))
    info_phone = int(input('Введите номер телефона: '))
    info_discription = str(input('Введите описание: '))

    if info_first_name == "" or info_second_name == "" or  (info_phone > 100000000000 and info_phone < 10000000000) or info_discription == "":
        print('Все строки должны быть заполнены - запись данных прервана')
        return
    with open('guide.txt', 'a', encoding="utf-8" ) as file:
        file.write(info_first_name + ', ' + info_second_name + ', ' + info_phone + ', ' + info_discription + '\n')
        file.close()
    