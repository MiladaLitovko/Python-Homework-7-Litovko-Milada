from add_info import new_info as add
from look_info import look as lk
from export import export_info as exp_inf
from import_inf import import_info as imp_inf
from search import search_info as search

number = 0
while number != 6:
    number = int(input('Введите действие, которое хотите совершить:\n 1 - добавление записи; \n 2 - просмотр записей; \n 3 - экспорт данных; \n 4 - импорт данных; \n 5 - Поиск записи; \n 6 - закончить работу \n Введите номер: '))
    if number == 1:
        add()
    if number == 2:
        lk()
    if number == 3:
        exp_inf()
    if number == 4:
        imp_inf()
    if number == 5:
        search()
    




    