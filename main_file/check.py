import os


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
