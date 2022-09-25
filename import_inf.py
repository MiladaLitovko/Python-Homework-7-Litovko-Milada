
def import_info():
    file = open('guide.txt', 'a', encoding="utf-8")
    new_file = open('import_file.txt', 'r', encoding="utf-8")
    line = new_file.readline()

 
    if len(line.split(', ')) == 4:
        file.write(line)
        for line in new_file:
            file.write(line)   
    else:
        user_info = line[:-1] + ', '
        for line in new_file:
            if line != '\n':
                user_info += line[:-1] + ', '
            else:
                file.write(user_info[:-2] + '\n')  
                user_info = ''
    file.close()
    new_file.close()