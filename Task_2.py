'''
Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов;
При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере;
- принимать параметр расширение исходного файла;
Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла;
- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''

import os

def rename_file_name(files_list: list, final_name: str, orig_extension: str, final_extension: str, orig_name_range: list):
    num = 0
    for obj in files_list:
        exten = obj.split(".")
        if exten[1] == orig_extension:

            num += 1
            temp = len(str(num))
            number = ''
            for _ in range(temp):
                number += '0'
            number += str(num)

            new_name = f'{final_name}{number}.{final_extension}'
            print(f'{obj= }')
            print(f'{new_name= }')
            os.rename(f'{obj}', f'{new_name}')

            print('--------------')
        else:
            print(f'{obj= }')


if __name__ == '__main__':
    files_list = ['testqwerty.txt', 'dataqwerty.txt', 'exampleqwerty.pdf']
    rename_file_name(files_list, "_TEST_", "txt", "md", [1, 4])