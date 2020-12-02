import os
import datetime
from pathlib import Path


class Date:
    def folderCreation(self, date_folder, Dir_PATH):
        for dates in date_folder:
            if dates == 0:
                WRAPPER_NAME = "day-0 to day-9"
            elif dates == 10:
                WRAPPER_NAME = "day-10 to day-19"
            elif dates == 20:
                WRAPPER_NAME = "day-20 to day-29"
            elif dates == 30:
                WRAPPER_NAME = "day-30 to day-39"
            elif dates == 40:
                WRAPPER_NAME = "day-40 to day-59"
            elif dates == 60:
                WRAPPER_NAME = "day-60 to day-89"
            else:
                WRAPPER_NAME = "From day-90"
            directories_path = os.path.join(Dir_PATH, WRAPPER_NAME)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)

    def onlyfile(self, files, Dir_PATH, only_files):
        for current_file in files:
            old_path = os.path.join(Dir_PATH, current_file)
            isFile = os.path.isdir(old_path)
            if isFile:
                continue
            only_files.append(current_file)

    def totaldays(self, only_files, Dir_PATH, mover):
        for file in only_files:
            mtime = (os.stat(os.path.join(Dir_PATH, file)).st_mtime)
            x = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            y = datetime.datetime.now().strftime('%Y-%m-%d')
            d1 = datetime.date(int(x[:4]), int(x[5:7]), int(x[8:]))
            d2 = datetime.date(int(y[:4]), int(y[5:7]), int(y[8:]))
            d3 = (d2-d1).days
            old_path = os.path.join(Dir_PATH, file)
            mover.append([d3, old_path, file])

    def moves(self, mover, Dir_PATH):
        for days, old_path, file in mover:
            isFile = os.path.isdir(old_path)
            if(isFile):
                continue
            if days >= 0 and days <= 9:
                WRAPPER_NAME = "day-0 to day-9"
                new_path = os.path.join(Dir_PATH, WRAPPER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 10 and days <= 19:
                WRAPPER_NAME = "day-10 to day-19"
                new_path = os.path.join(Dir_PATH, WRAPPER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 20 and days <= 29:
                WRAPPER_NAME = "day-20 to day-29"
                new_path = os.path.join(Dir_PATH, WRAPPER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 30 and days <= 39:
                WRAPPER_NAME = "day-30 to day-39"
                new_path = os.path.join(Dir_PATH, WRAPPER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 40 and days <= 59:
                WRAPPER_NAME = "day-40 to day-59"
                new_path = os.path.join(Dir_PATH, WRAPPER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 60 and days <= 89:
                WRAPPER_NAME = "day-60 to day-89"
                new_path = os.path.join(Dir_PATH, WRAPPER_NAME, file)
                os.rename(old_path, new_path)
            else:
                WRAPPER_NAME = "From day-90"
                new_path = os.path.join(Dir_PATH, WRAPPER_NAME, file)
                os.rename(old_path, new_path)

    def extrafolder(self, Dir_PATH):
        folders = list(os.walk(Dir_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def DATE(Dir_PATH):
    files = os.listdir(Dir_PATH)
    only_files = []
    date_folder = [0, 10, 20, 30, 40, 60, 90]
    mover = []
    obj = Date()
    obj.folderCreation(date_folder, Dir_PATH)
    obj.onlyfile(files, Dir_PATH, only_files)
    obj.totaldays(only_files, Dir_PATH, mover)
    obj.moves(mover, Dir_PATH)
    obj.extrafolder(Dir_PATH)
