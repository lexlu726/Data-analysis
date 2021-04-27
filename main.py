import pandas as pd
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt

data_frame = pd.read_csv("StarWars.csv",encoding = "ISO-8859-1")

data = {}

data2 = defaultdict(list)
data2["episode"].append("I")
data2["episode"].append("II")
data2["episode"].append("III")
data2["episode"].append("IV")
data2["episode"].append("V")
data2["episode"].append("VI")



seen = pd.DataFrame(data_frame, columns = ["Which of the following Star Wars films have you seen? Please select all that apply.","Unnamed: 4", "Unnamed: 5","Unnamed: 6","Unnamed: 7","Unnamed: 8"])
e1 = seen["Which of the following Star Wars films have you seen? Please select all that apply."]
e2 = seen["Unnamed: 4"]
e3 = seen["Unnamed: 5"]
e4 = seen["Unnamed: 6"]
e5 = seen["Unnamed: 7"]
e6 = seen["Unnamed: 8"]
test = seen[["Which of the following Star Wars films have you seen? Please select all that apply.","Unnamed: 4"]]


def convertit(x):
    if type(x) == str:
        return 1
    else:
        return 0

I = e1.apply(convertit)
II = e2.apply(convertit)
III = e3.apply(convertit)
IV = e4.apply(convertit)
V = e5.apply(convertit)
VI = e6.apply(convertit)


def sumup(x):
    listr = []
    l = 0
    for s in x:
        listr.append(s)
    r = tuple(listr)
    allin = sum(r)
    
    result = (allin * 100) / 1187
    return int(result)

episode_I = data2["result"].append(sumup(I))
episode_II = data2["result"].append(sumup(II)) 
episode_III = data2["result"].append(sumup(III))
episode_IV = data2["result"].append(sumup(IV)) 
episode_V = data2["result"].append(sumup(V))
episode_VI = data2["result"].append(sumup(VI))


df = pd.DataFrame(data2, columns = ["episode", "result"])


sns.set()

sns.lineplot(data=df, x="episode", y="result")

plt.show()