import os
from pathlib import Path


class ExtOrganize:
    def extension(self, Dir_PATH, File_extension, ALL_FILES):
        for FILES in ALL_FILES:
            file_path = Path(FILES)
            REMOVIND_DOT = file_path.suffix.lower()
            REMOVIND_DOT = REMOVIND_DOT[1::]
            File_extension.append(REMOVIND_DOT)

    def directoryCreation(self, File_extension, Dir_PATH):
        for D in File_extension:
            directories_path = os.path.join(Dir_PATH, D)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)

    def movables(self, ALL_FILES, Dir_PATH):
        for FILES in ALL_FILES:
            file_path = Path(FILES)
            EXTENSION = file_path.suffix.lower()
            EXTENSION = EXTENSION[1::]
            old_path = os.path.join(Dir_PATH, file_path)
            new_path = os.path.join(Dir_PATH, EXTENSION, FILES)
            os.rename(old_path, new_path)

    def extrafolder(self, Dir_PATH):
        folders = list(os.walk(Dir_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def EXT(Dir_PATH):
    ALL_FILES = os.listdir(Dir_PATH)
    File_extension = []
    obj = ExtOrganize()
    obj.extension(Dir_PATH, File_extension, ALL_FILES)
    obj.directoryCreation(File_extension, Dir_PATH)
    obj.movables(ALL_FILES, Dir_PATH)
    obj.extrafolder(Dir_PATH)
