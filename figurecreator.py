import matplotlib.pyplot as plt
from processdata import datacollector

def firgurecreat(data, question):
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
    print(f"the fig question is {question}")
    fgname = input("please input the figname: ")
    return plt.savefig(f"./image/{fgname}.jpg")



# firgurecreat({'Response': 0.08431703204047218, 'Yes': 78.83642495784149, 'No': 21.079258010118043})
