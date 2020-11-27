from check import main
from jfile_organizer import Dictionary


class Execute:
    def __init__(self, path, y):
        self.Dir_PATH = path
        self.Src_PATH = path
        self.B = y
        if y >= 5:
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
        print("Select 4 for to convert organized files into junk files\n")
        print("If you are done press enter\n")
        A = input("ENTER PATH\n")
        A = r''+A+'\\'
        if len(A) == 1:
            break
        B = int(input("Enter Your Choice\n"))
        obj = Execute(A, B)
        obj.Run()
