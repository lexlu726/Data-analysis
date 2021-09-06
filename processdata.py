import pandas as pd
from collections import defaultdict
import seaborn as sns

data_frame = pd.read_csv("C:/Users/Asus/OneDrive/Desktop/program/Data-Analysis/Data-analysis/StarWars.csv ",encoding = "ISO-8859-1")

# class Node:
#     def __init__(self, data = None ):
#         self.data = data
#         self.nextval = None

class datacollector:
     
    def __init__(self):
        self.title = []# it contains title which unname been fix
        self.info = None# it contains each question(title)'s result by percentage'
        self.unchange = []
    
    #collecting the title into dict and follow with number. assuming first row as title.
    def collecttitle(self, data):
        temp = "" 
        e = 1 #numbering same question 
        for i in data: #it classify title with loop 
            # if "Unnamed:" in i :
            #      print("yes")
            self.unchange.append(i)
            if i not in self.title:
                if "Unnamed:"  not in i:
                    self.title.append(i)
                    temp = i 
                    e =1
                else: #saving title temperally and fill unamed space with title which in same question with previous one
                    i = temp + f"({e})"
                    e += 1 
                    self.title.append(i)
            
        return self.title

        #a function to breakdown data by title and count each subject's votes had
    def collectinfo(self,target):
        tem = []
        #create pointer that 
        pointer = pd.DataFrame(data_frame, columns = [self.unchange[target]])
        for item in pointer[self.unchange[target]]:

            if len(tem) <= len(pointer):
                tem.append(item)

        tem = self.countit(tem)
        self.info = tem


        return self.info

    #function which prove a range of colum data search
    # def mudata(self, start ,end):
    #     if end > len(self.title) or start == 0:
    #         print(f"it is out of range. please choose from 1 to {len(self.title)}")
    #     elif start > end:
    #         print("start should not higher than end")
    #     for n in range(start, end):
    #         if 0< start < len(self.title) and len(self.title)>= end:
    #             self.collectinfo(n)

    #     return self.info

    def countit(self, a):
        result = {"skip": 0}
        d = []
        for i in a:
            if type(i) == float:
                result["skip"] += 1 
            elif i not in result:
                result.update({i:1})
            else:
                result[i] += 1 
        for r in result:
            if result[r] <5 and r != "Response" and len(r)< 8 :
                result["skip"] += 1
                d.append(r)

        for item in d:
            result.pop(item)
        for t in result:
            result[t] = float((result[t] * 100) / 1186)

        return result 

    def printout(self):
        target = {}
        p = []
        i = []
        for item in range(len(self.info)):
            print(item)
            if self.info[item] not in target:
                pass

        
    



# test = datacollector()
# test.collecttitle(data_frame)
# # print(test.title)
# test.collectinfo(2)

# print(test.info)

# for i in test.title:
#     print(test.title[i])

# print(test.printout())

