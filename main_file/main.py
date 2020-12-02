import os
from jfile_organizer import Dictionary


class Check:
    def file_check(self, Src_PATH, Dir_PATH):
        for path, _, files in os.walk(Src_PATH):
            if files:
                for Files in files:
                    if not os.path.isfile(Dir_PATH+Files):
                        os.rename(path+'\\'+Files, Dir_PATH+Files)

    def folder_remove(self, Dir_PATH):
        folders = list(os.walk(Dir_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def main(Src_PATH, Dir_PATH):
    if len(Src_PATH) == 1:
        print("Enter a valid Path")
        return
    if not os.path.exists(Src_PATH):
        print("Enter a valid path")
        return
    obj = Check()
    obj.file_check(Src_PATH, Dir_PATH)
    obj.folder_remove(Dir_PATH)


class Execute:
    def __init__(self, path, y):
        self.Dir_PATH = path
        self.Src_PATH = path
        self.B = y
        if y >= 4:
            print("Enter the Valid Choice")
            return
        main(self.Src_PATH, self.Dir_PATH)

    def Run(self):
        if self.B >= 4:
            return
        Dictionary(self.Dir_PATH, self.B)


if __name__ == "__main__":
    while True:
        print("\nSelect 1 for organizing files with extension\n")
        print("Select 2 for organizing files with dates\n")
        print("Select 3 for organizing files with size\n")
        print("If you are done press enter\n")
        A = input("ENTER PATH\n")
        A = r''+A+'\\'
        if len(A) == 1:
            break
        B = int(input("Enter Your Choice\n"))
        obj = Execute(A, B)
        obj.Run()
