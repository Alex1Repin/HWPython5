# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W

encod = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
code = '12W1B12W3B24W1B14W'

def write_file(fl):# Создал файл
     with open ('Task04_03_05.txt', 'w') as data:
          data.write(fl)

write_file(encod)

file1 = 'Task04_03_05.txt'

def read_pol(file):  # Получение данных из файла
    with open(file, 'r') as data:
        pol = data.readline()
    return pol

encodes = read_pol(file1)

def encode(decode_string):
    encode_string = ''
    count = 1
    char = decode_string[0]
    for i in range(1, len(decode_string)):
        if decode_string[i] == char:
            count +=1
        else:
            encode_string = encode_string + str(count) + char
            char = decode_string[i]
            count = 1
            encode_string = encode_string + str(count) + char
    return encode_string

decodes = encode(encodes)

def write_file(fl):# перезаписал в файл
     with open ('decode_Task04_03_05.txt', 'w') as data:
          data.write(fl)

write_file(decodes)

#Декодируем
def write_file(fl):# Создал файл
     with open ('Task04_04_05.txt', 'w') as data:
          data.write(fl)

write_file(code)

file2 = 'Task04_04_05.txt'

def read_pol(file):  # Получение данных из файла
    with open(file, 'r') as data:
        pol = data.readline()
    return pol

decodes = read_pol(file2)

def decode(encode):
    decode_str = ''
    anti_char = ''
    for i in range(len(encode)):
        if encode[i].isdigit():
            anti_char += encode[i]
        else:
            decode_str += encode[i] * int(anti_char)
        anti_char = ''
    return decode_str

encodes = decode(decodes)

def write_file(fl):# перезаписал в файл
     with open ('encode_Task04_04_05.txt', 'w') as data:
          data.write(fl)

write_file(encodes)

