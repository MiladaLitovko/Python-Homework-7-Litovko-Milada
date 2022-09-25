def search_info():
    number = int(input('По какому полю хотите искать запись: 0 - Фамилия, 1 - Имя, 2 - Номер телефона, 3 - Описание \n Введите номер поля: '))
    if number > 3:
        print('Неверно введенная цифра - поиск прерван')
        return
    enter_info = str(input('Введите строку поиска: '))
    with open('guide.txt', 'r', encoding="utf-8" ) as file:
        for line in file:
            if enter_info.upper() in line.split(', ')[number].upper() and number != 3:
                print(line)
            elif number == 3 and enter_info.upper() in line.split(', ')[number][:-1].upper():
                print(line)


    file.close()