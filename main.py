import pandas as pd
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt
from processdata import datacollector

data_frame = pd.read_csv("StarWars.csv",encoding = "ISO-8859-1")


def firgurecreat(data):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = []
    sizes = []
    time = []
     # only "explode" the 2nd slice (i.e. 'Hogs')
    
    for item in data:
        if data[item]> 1:
            labels.append(item)
            sizes.append(data[item])
            time.append(0)
    print(labels, sizes,time)
    explode = tuple(time)



    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    return plt.savefig(f"{test.title[10]}.jpg")



# firgurecreat({'Response': 0.08431703204047218, 'Yes': 78.83642495784149, 'No': 21.079258010118043})

if __name__ == '__main__':
    pass
    test = datacollector()
    test.collecttitle(data_frame)
    test.collectinfo(10)
    print(test.info)
    firgurecreat(test.info)
    
