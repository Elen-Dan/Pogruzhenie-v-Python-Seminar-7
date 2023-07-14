'''
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
'''

import os

from Task_2 import rename_file_name
from Task_5 import create_files_with_extension
from Task_6 import create_dif_files
from Task_7 import group

if __name__ == '__main__':
    create_files_with_extension('bin') # создание файлв с указанным расширением.
    create_dif_files(txt=2, bin=4, png=8) # создание файлов с разными расширениями
    group(os.getcwd()) # сортировка файлов по каталогам