'''
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 
При необходимости, программа должна уметь импортировать записи из файла, который сама экспортировала.

под форматами понимаем структуру файлов, например:
в файле на одной строке хранится одна часть записи, пустая строка - разделитель
Фамилия_1
Имя_1
Телефон_1
Описание_1
<пустая строка>
Фамилия_2
Имя_2
Телефон_2
Описание_2
<пустая строка>
и т.д.
.
или в файле на одной строке хранится все записи, символ разделитель - *;***
.
Фамилия_1,Имя_1,Телефон_1,Описание_1
Фамилия_2,Имя_2,Телефон_2,Описание_2
и т.д.
.
Обязательные пункты меню:
1 Просмотр записей
2 Добавление записи
3 Экспорт (не менее двух форматов)
4 Импорт (не менее двух форматов)
5 Выход из программы (программа должна работать, пока пользователь сам не выйдет из неё)
.
Также приветствуется:
- Поиск записи
- Удаление записи


Сами выбираем как хранятся записи - 
Импорт - я могу в какой-то файл (создать новый) и в него написал запись  ==> и это будет добавляться в справочник - 2 вида импорта
Экспорт - как-то храним у себя данные (введите 1 - если хотите получить в таком формате или введите 2 - если хотите в таком ==> и затем появляется файл в том формате, который выбрали)
Резервная копия?
'''