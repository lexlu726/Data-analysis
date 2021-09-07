import pandas as pd
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt
from processdata import datacollector
from figurecreator import firgurecreat

data_frame = pd.read_csv("StarWars.csv",encoding = "ISO-8859-1")


test = datacollector()
test.collecttitle(data_frame)
if __name__ == '__main__':

    test.collectinfo(10)
    print(test.info)
    firgurecreat(test.info, test.pointer)
    
