# -*- coding: utf-8 -*-

import os, time, shutil
import zipfile as zp


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class PhotosSorter:

    def unzip_files(self, file):
        with zp.ZipFile(file, 'r') as file_z:
            file_z.extractall()

    def sort_files(self, dir_to_scan, scanned_files_dir):
        if not os.path.isdir(os.path.join(scanned_files_dir, 'icons_by_year')):
            os.makedirs(os.path.join(scanned_files_dir, 'icons_by_year'))
        for dirpath, dirnames, filenames in os.walk(dir_to_scan):
            for img in filenames:
                img_path = os.path.join(dirpath, img)
                time_of_creation = time.gmtime(os.path.getmtime(img_path))[0:2]
                final_dir = os.path.join(scanned_files_dir, 'icons_by_year', str(time_of_creation[0]),
                                         str(time_of_creation[1]))
                if not os.path.isdir(final_dir):
                    os.makedirs(final_dir)
                shutil.copy2(img_path, final_dir)


icons_folder = os.path.normpath('C:/Users/igorek/PycharmProjects/python_base/lesson_009/icons')
final_folder = os.path.normpath('C:\\Users\igorek\PycharmProjects\python_base\lesson_009')

a = PhotosSorter()
a.sort_files(icons_folder, final_folder)

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
