import pandas as pd
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
        self.infopointer = None

    def selectfile(self):
        fn = []
        while len(onlyfiles)>=1:
            self.fname = input("please enter the file's name in image folder: ")
            # print("i am at 1st floor")
            for item in onlyfiles:
                # print("i am at for loop ")
                tem = item.split(".csv")
                if tem[0] not in fn:
                    fn.append(tem[0])
                    continue
            if self.fname in fn:
                self.csv = pd.read_csv(f"./test-subject/{self.fname}.csv",encoding = "ISO-8859-1")
                break
            else:
                print(f"there has no file name call : {self.fname}")
                print(f"the CSV file in the folder is : {fn}")      
        return self.csv

    def selectinfo(self):
        test = datacollector()
        test.collecttitle(self.csv)
        while test:
            qnumber = input("please enter number which question you want: ")
            try:
                test.collectinfo(int(qnumber), self.csv)
            except ValueError:
                print("please enter the interger.")
            except IndexError:
                print("the number is out of range.")      
            finally:
                break

        try:
            return firgurecreat(test.info, test.pointer)
        except TypeError:
            self.selectinfo()


if __name__ == '__main__':
    aq = questionuser()
    aq.selectfile()
    aq.selectinfo()

