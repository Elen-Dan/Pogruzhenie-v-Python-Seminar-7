'''
Задание № 6
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
'''

from pathlib import Path
import os, random, string

def create_files_with_extension(extension, min_name_lenght=6, max_name_lenght=30, min_file_size=256, max_file_size=4096, num_files=1):
    for _ in range(num_files):
        name_lenght = random.randint(min_name_lenght, max_name_lenght)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_lenght)) + '.' + extension

        file_size = random.randint(min_file_size, max_file_size)
        random_bytes = os.urandom(file_size)
        # random_bytes = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size)).encode('UTF-8')

        with open(file_name, 'wb') as file:
            file.write(random_bytes)

def create_dif_files (**kwargs):
    for ext, num in kwargs.items():
        create_files_with_extension(ext, num_files=num)

def create_dir(name_dir: str):
    name = Path(Path.cwd() / name_dir)
    if not name.exists():       #проверка на наличие директория
        name.mkdir()            #создает директорий с именем name_dir в текущем директории
    os.chdir(name)          #переходим в созданный каталог сделав его текущим


if __name__ == '__main__':
    create_dif_files(txt=2, bin=4, png=8)
    create_dir('new')