from extension import EXT
from date import DATE
from size import SIZEORGANIZER
import os


class jfileOrganizer:
    def __init__(self):
        self.Dir_PATH = 'C:\\Users\\samhi\\Desktop\\testing'+'\\'
        self.Src_PATH = r'C:\Users\samhi\Desktop\testing'+'\\'

    def extension(self, v):
        EXT(v)

    def DATES(self, v):
        DATE(v)

    def SIZE(self, v):
        SIZEORGANIZER(v)


def Dictionary(A, B):
    d = {1: "ORGANIZED BY Extension\n",
         2: "ORGANIZED BY DATE\n",
         3: "ORGANIZED BY SIZE\n"}
    if len(A) == 1 or len(A) == 0:
        return
    if not os.path.exists(A):
        return
    inputChoice(A, B)
    print(d[B])


def inputChoice(A, B):
    obj = jfileOrganizer()
    if B == 1:
        obj.extension(A)
    if B == 2:
        obj.DATES(A)
    if B == 3:
        obj.SIZE(A)
    if B > 3:
        print("your selection is not valid")
