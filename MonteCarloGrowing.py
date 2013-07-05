#Elizabeth Mahon
#Monte Carlo simulation (?) that reassigns the year/%non growing season
#then calculates the slope for each configuration
#Then chucks it in a bin and makes a histogram
#This should end up showing that the actual value is fairly unlikely

import matplotlib.pyplot as pyplot
import numpy as np
from RecentLeastSquares import LeastSquares
from RecordReader import RecordReader
from Covariance import Covariance
import random

def MonteCarloGrowing(folder, master):
    data = RecordReader(folder, master)
    index = data.keys()

    diversions = list()
    growdiv = list()
    percents = list()
    years = list()
    all_delta = list()
    trials = 10000000 #chosen arbitrarily
    bins = dict()
    p = 0.0

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

    #calculate original percents
    for n in range(62):
        percents.append((1 - (growdiv[n]/diversions[n])) *100)
        years.append(1950+n)

    #get original least squares fit
    deltastar = LeastSquares(zip(years,percents))

    #randomize percents....
    for i in range(trials):
        rand = random.sample(percents, len(percents))
        slope, intercept = LeastSquares(zip(years, rand))
        all_delta.append(slope)

    for m in all_delta:
        if m > deltastar[0]:
            p += 1
    
    likely = p/trials #likelihood we would get the calculated slope randomly....
    print deltastar
    print likely

    #make bins
    maximum = max(all_delta)
    binvals = np.linspace(0,maximum, endpoint = True)
    print maximum

    for val in binvals:
        bins[val] = 0

    for delta in all_delta:
        for q in range(len(binvals)-1):
            if ((delta < binvals[q+1]) and (delta > binvals[q])):
                bins[binvals[q]] += 1

    wid = ((binvals[1] - binvals[2])/2)
    pyplot.bar(bins.keys()-wid, bins.values(),width = wid)
    pyplot.show()

MonteCarloGrowing('/home/elizabeth/Dropbox/Windows-LinuxShare/','PercentStructures.csv')
