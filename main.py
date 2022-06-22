import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

populationmean = st.mean(data)
populationstd = st.stdev(data)
print(f"Population mean:{populationmean}")
print(f"Population std:{populationstd} \n")

fig = ff.create_distplot( [data], ["Temperature"], show_hist = False)
#fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):  
        random_index = random.randint(0, len(data)-1) #5
        value = data[random_index] #data[5]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean
    
def setup():
    meanlist= []
    for i in range(0, 1000):
        f = random_set_of_mean(100)
        meanlist.append(f)
    mean = st.mean(meanlist)
    std = st.stdev(meanlist)
    print(f"Sample mean:{mean}")
    print(f"Sample std:{std}")

    fig = ff.create_distplot( [meanlist], ["Sample Temperature data"], show_hist = False)
    fig.show()

setup()
#the sample mean is equal to the population mean
#Standard deviation of the sampling mean = 1/10 of Population Standard deviation