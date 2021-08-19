import pandas as pd
from collections import defaultdict

data_frame = pd.read_csv("C:/Users/Asus/OneDrive/Desktop/program/Data-Analysis/Data-analysis/StarWars.csv ",encoding = "ISO-8859-1")

# class Node:
#     def __init__(self, data = None ):
#         self.data = data
#         self.nextval = None

class datacollector:
    def __init__(self):
        self.title = {}
        self.info = {}
    
    def collecttitle(self, data):
        n = 0 
        for i in data:
            if i not in self.title:
                self.title.update({n:i})
                n+= 1
        return self.title

        #work on that data one by one 
    def collectinfo(self,target):
        tem = []
        pointer = pd.DataFrame(data_frame, columns = [self.title[target]])
        for item in pointer[self.title[target]]:

            if len(tem) <= len(pointer):
                tem.append(item)
        tem = self.countit(tem)
        self.info.update({self.title[target]:tem})


        return self.info

    #function which prove a range of colum data search
    def mudata(self, start ,end):
        if end > len(self.title) or start == 0:
            print(f"it is out of range. please choose from 1 to {len(self.title)}")
        elif start > end:
            print("start should not higher than end")
        for n in range(start, end):
            if 0< start < len(self.title) and len(self.title)>= end:
                self.collectinfo(n)

        return self.info

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
        return result 

    def printout(self):
        for title, item in self.info.keys() and self.info.items():
            print(title,":",end ="")
            print(item)
            print("")
        return     




test = datacollector()
test.collecttitle(data_frame)
test.mudata(1, 30)
print(test.printout())

