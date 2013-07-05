#Elizabeth Mahon
#Make a CDF for a year

from RecordReader import RecordReader
import matplotlib.pyplot as pyplot
import numpy as np

def CDF(yeardata):
    tot = 0
    cdf = list()

    for n in range(len(yeardata)):
        tot += yeardata[n]
        cdf.append(float(tot/sum(yeardata)))

    return cdf

def main(folder, master):
    data = RecordReader(folder, master)

    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

    diversions = dict()
    index = data.keys()

    for i in range(62):
        mon = list()
        for j in range(12):
            #next part necessary because there's a bit of imprecision introduced in the indexes somewhere, so I can't just recalculate them
            for thing in index:
                if(thing < (i+1950+.01*(j+1)+.005) and thing > (i+1950+.01*(j+1)-.005)):
                    mon.append(data[thing])
        diversions[i+1950] = mon

    year1 = 1952;
    year2 = 2008;

    pyplot.plot(CDF(diversions[year1]))
    pyplot.ylabel("Diversions over Year",fontsize=15)
    pyplot.xlabel("Months",fontsize=15)
    pyplot.title("Cumulative Diversions in Two Years",fontsize=20)
    pyplot.xticks(np.arange(12),months)
    pyplot.plot(CDF(diversions[2008]))
    pyplot.legend([str(year1), str(year2)])
    pyplot.show()

main('/home/elizabeth/Dropbox/elizabeth.mahon/Data/','PercentStructures.csv')
