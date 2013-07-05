#Elizabeth Mahon
#Computational Probability and Statistics
#Calculate and graph the percentage of river water used per year

from FlowReader import FlowReader
from RecordReader import RecordReader
import matplotlib.pyplot as pyplot
import numpy as np

def PercentageGrapher(folder, master, flowfile):
    data = RecordReader(folder, master)
    flow = FlowReader(folder+flowfile)
    diversions = list()
    yearflow = list()
    percentages = list()
    labels = list()
    width = .1
    index = data.keys()
    dex = flow.keys()

    for q in range(62):
        diversions.append(0)
        yearflow.append(0)

    ind = np.arange(62)

    for i in range(62):
        for j in range(12):
            yearflow[i] += float(flow[(str(i+1950)+'-'+('{0:{fill}2}'.format(j+1,fill='0')))])
            #next part necessary because there's a bit of imprecision introduced in the indexes somewhere, so I can't just recalculate them
            for thing in index:
                if(thing < (i+1950+.01*(j+1)+.005) and thing > (i+1950+.01*(j+1)-.005)):
                    diversions[i] += data[thing]

    for n in range(62):
        percentages.append((diversions[n]/yearflow[n])*100)
        labels.append(1950+n)

    pyplot.plot(ind, percentages)
    pyplot.xlim(0,len(ind))
    pyplot.xticks(ind+width,labels,rotation='vertical')
    pyplot.xlabel("Year", fontsize ="15")
    pyplot.ylabel("Percentage of Water Diverted",fontsize="15")
    pyplot.title("Percentage Diverted Over Time",fontsize="20")
    pyplot.show()

PercentageGrapher('/home/elizabeth/Dropbox/Windows-LinuxShare/','PercentStructures.csv','PoudreFlow.csv')
