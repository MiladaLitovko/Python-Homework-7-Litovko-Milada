
def export_info():
    number = int(input('Выберите формат показа данных: \n1: Фамилия, Имя, Телефон, Описание \n2: \nФамилия \nИмя \nТелефон \nОписание \nВведите номер формата: '))
    file = open('guide.txt', 'r', encoding="utf-8")
    new_file = open('export_file.txt', 'w', encoding="utf-8")
 
    if number == 1:
        for line in file:
            new_file.write(line)   
    elif number == 2:
       for line in file:
            info = line.split(', ')
            for i in info:
                new_file.write(i + '\n')   
            # new_file.write('\n')
    else:
        file.close()
        new_file.close()
        print('Неверно введенная цифра - экспорт данных прерван')
        return
    file.close()
    new_file.close()
