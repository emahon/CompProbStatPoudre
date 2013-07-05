#Elizabeth Mahon
#Graph percentage of water diverted outside the growing season over time

import matplotlib.pyplot as pyplot
import numpy as np
from RecentLeastSquares import LeastSquares
from RecordReader import RecordReader

def GrowingSeasonGrapher(folder, master):
    data = RecordReader(folder, master)
    index = data.keys()

    diversions = list()
    growdiv = list()
    percents = list()
    labels = list()
    fit = list()
    ind = list()

    for k in range(62): #make room for each year in structures
        diversions.append(0)
        growdiv.append(0)

    #get data for growing season
    for i in range(62):
        for j in range(12):
            #next part necessary because there's a bit of imprecision introduced in the indexes somewhere, so I can't just recalculate them
            for thing in index:
                if(thing < (i+1950+.01*(j+1)+.005) and thing > (i+1950+.01*(j+1)-.005)):
                    diversions[i] += data[thing]
                    if (j < 10 and j > 3): #growing season
                        growdiv[i] += data[thing]

    for n in range(62):
        percents.append((1 - (growdiv[n]/diversions[n])) *100)
        labels.append(1950+n)
        ind.append(n)

    #get least squares fit
    slope, intercept = LeastSquares(zip(labels,percents))
    print slope, intercept

    for value in labels:
        fit.append(value*slope + intercept)

    pyplot.plot(ind, percents)
    pyplot.plot(ind, fit)
    pyplot.xlim(0,62)
    pyplot.xticks(np.arange(62), labels,rotation=90)
    pyplot.legend(("Data","Least Squares Fit"), loc = "upper left")
    pyplot.xlabel("Year", fontsize ="15")
    pyplot.ylabel("Percentage of Water Diverted Outside the Growing Season",fontsize="15")
    pyplot.title("Percentage Diverted Outside the Growing Season Over Time",fontsize="20")
    pyplot.show()

GrowingSeasonGrapher('/home/elizabeth/Dropbox/Windows-LinuxShare/','PercentStructures.csv')
