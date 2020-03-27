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

ICONS_FOLDER = os.path.normpath('C:\\Users\igorek\PycharmProjects\python_base\lesson_009\icons.zip')

FINAL_FOLDER = os.path.normpath('C:\\Users\igorek\PycharmProjects\python_base\lesson_009')


class PhotosSorter:

    def __init__(self, scanned_files_dir, dir_to_scan):
        self.scanned_files_dir = scanned_files_dir
        self.dir_to_scan = dir_to_scan

    def unzip_files(self, file):
        with zp.ZipFile(file, 'r') as file_z:
            file_z.extractall()

    def create_end_folder(self):
        if not os.path.isdir(os.path.join(self.scanned_files_dir, 'icons_by_year')):
            os.makedirs(os.path.join(self.scanned_files_dir, 'icons_by_year'))
            # TODO Дублируете код - джойните дважды один и тот же путь. Создайте атрибут для полного пути к папке один
            #  и раз соберите путь и используйте далее сколько угодно раз (в разных местах ниже встречается ещё не раз).
            #  Кстати, имя папки это глобальная константа

    def sort_files(self):
        for dirpath, dirnames, filenames in os.walk(self.dir_to_scan):
            for img in filenames:
                img_path = os.path.join(dirpath, img)
                time_of_creation = time.gmtime(os.path.getmtime(img_path))[0:2]
                final_dir = os.path.join(self.scanned_files_dir, 'icons_by_year', str(time_of_creation[0]),
                                         str(time_of_creation[1]))
                if not os.path.isdir(final_dir):
                    os.makedirs(final_dir)
                shutil.copy2(img_path, final_dir)

    def sort(self):
        self.create_end_folder()
        self.sort_files()


class PhotosSorterZip(PhotosSorter):

    def __init__(self, scanned_files_dir, dir_to_scan):
        super().__init__(scanned_files_dir, dir_to_scan)

    def zip_namelist(self):
        with zp.ZipFile(self.dir_to_scan, 'r') as myzip:
            return myzip.namelist()

    def get_date(self, file_name):
        with zp.ZipFile(self.dir_to_scan, 'r') as myzip:
            return myzip.getinfo(file_name).date_time

    def get_obj_info(self, file_name):
        with zp.ZipFile(self.dir_to_scan, 'r') as myzip:
            return myzip.getinfo(file_name)

    def check_folder_existence(self, final_dir):
        if not os.path.isdir(final_dir):
            os.makedirs(final_dir)

    def extract_image(self, filename, final_dir):
        with zp.ZipFile(self.dir_to_scan, 'r') as myzip:
            return myzip.extract(member=filename, path=final_dir)

    def sort_files(self):
        for filename in self.zip_namelist():
            if filename[-3:] == 'png':
                date = self.get_date(filename)
                final_dir = os.path.join(self.scanned_files_dir, 'icons_by_year',
                                         str(date[0]), str(date[1]))
                self.check_folder_existence(final_dir)
                self.extract_image(filename, final_dir)
                break  # TODO Cкопировали один файл и на отдых? :) Чем обосновано?

    def sort(self):
        self.create_end_folder()
        self.sort_files()


a = PhotosSorterZip(FINAL_FOLDER, ICONS_FOLDER)
a.sort_files()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
