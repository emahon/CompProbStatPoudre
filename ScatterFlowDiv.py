#Elizabeth Mahon
#Make a scatter plot of diversions versus flow

from FlowReader import FlowReader
from RecordReader import RecordReader
import matplotlib.pyplot as pyplot
import numpy as np

def ScatterFlowDiv(folder, master, flowfile):
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

    for i in range(62):
        for j in range(12):
            yearflow[i] += float(flow[(str(i+1950)+'-'+('{0:{fill}2}'.format(j+1,fill='0')))])
            #next part necessary because there's a bit of imprecision introduced in the indexes somewhere, so I can't just recalculate them
            for thing in index:
                if(thing < (i+1950+.01*(j+1)+.005) and thing > (i+1950+.01*(j+1)-.005)):
                    diversions[i] += data[thing]

    pyplot.scatter(yearflow, diversions)
    pyplot.xlabel("Flow in Poudre (acre-feet)", fontsize ="15")
    pyplot.ylabel("Diversions from Poudre (acre-feet)",fontsize="15")
    pyplot.title("Relationship between Flow and Diversions",fontsize="20")
    pyplot.show()

ScatterFlowDiv('/home/elizabeth/Dropbox/Windows-LinuxShare/', 'PercentStructures.csv','PoudreFlow.csv')


