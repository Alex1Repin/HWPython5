#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из этого абв текста \
все вабвс слова, содерабващие содержащие "абв"'

def write_file(fl):
     with open ('Task01_02_05.txt', 'w', encoding='utf-8') as data:
          data.write(fl)
write_file(my_text)

file1 = 'task01_02_05.txt'

def read_pol(file):  # Получение данных из файла
    with open(file, 'r', encoding='utf-8') as data:
        pol = data.readline()
    return pol

tex = read_pol(file1)

def del_some_words(text):
    my_tex = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(my_tex)

text1 = del_some_words(tex)
print(my_text)
print(text1)