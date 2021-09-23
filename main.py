import pandas as pd
import sys
from collections import defaultdict
import matplotlib.pyplot as plt
from processdata import datacollector
from figurecreator import firgurecreat
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir("./test-subject") if isfile(join("./test-subject", f))]


class questionuser: 
    def __init__(self):
        self.fname = None
        self.csv = None

    def selectfile(self):
        fn = []
        while len(onlyfiles)>=1:
            self.fname = input("please enter the file you want to analysis: ")
            # print("i am at 1st floor")
            for item in onlyfiles:
                # print("i am at for loop ")
                tem = item.split(".csv")
                fn.append(tem[0])
                if self.fname == tem[0]:
                    self.csv = pd.read_csv(f"./test-subject/{self.fname}.csv",encoding = "ISO-8859-1")
                    break
                

            if self.fname in fn:
                print("True")
                break
            else:
                print(f"there has no file name call : {self.fname}")
                print(f"the CSV file in the folder is : {fn}")

                    
        return self.csv




aq = questionuser()
print(aq.selectfile())

# f = input("please enter the file you want to analysis: ")
# try:
#      data_frame = pd.read_csv(f"./test-subject/{f}.csv",encoding = "ISO-8859-1")
        
# except :
#     print("the file name can not be found ")

# try:
#     q = int(input("please enter number that question you want to analysis: "))
# except:
#     print("enter number")

# try:
#     q = questionuser()
# except FileNotFoundError:
#     print("there has no such file")

# from os import walk

# filenames = next(walk("./test-subject"), (None, None, []))[2]  # [] if no file

# print(filenames)




# if __name__ == '__main__':
#     test = datacollector()
#     test.collecttitle(data_frame)
#     test.collectinfo(q, data_frame)
#     print(test.info)
#     firgurecreat(test.info, test.pointer)
    
