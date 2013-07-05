#Elizabeth Mahon
#Takes the 2003-2011 dataset and randomizes it
#Calculates the linear least squares fit for the randomizations
#Tells us how likely the increase in the actual data is

from RecordReader import RecordReader
from Covariance import Covariance
import random

def RecentLeastSquares(folder, master):
    data = RecordReader(folder, master)
    values = list()
    years = list()
    all_delta = list()
    p = 0.0
    trials = 3628800 #10!

    for i in range(9):
        values.append(0)
        years.append(i+2003)

    for key in data.keys():
        if (int(key) > 2002):
            values[(int(key) - 2003)] += data[key]

    deltastar = LeastSquares(zip(years,values))
    print deltastar

    for i in range(trials):
        rand = random.sample(values, len(values))
        all_delta.append(LeastSquares(zip(years, rand)))

    #probability we would get a slope as large as the observed one randomly
    all_m, all_b = zip(*all_delta)
    for m in all_m:
        if m > deltastar[0]:
            p += 1

    return p/trials

def LeastSquares(values):
    #calculate least squares

    all_x, all_y = zip(*values)

    #sample means; might have to edit this
    meanx = (sum(all_x)/float(len(all_x)))
    meany = (sum(all_y)/float(len(all_y)))

    #Variance of x
    diff = 0.0
    for x in all_x:
        diff += (x - meanx)**2
    varx = (1.0/len(all_x))*diff

    #Covariance of x and y
    cov = Covariance(values)

    slope = cov/varx
    intercept = meany - slope*meanx

    return slope, intercept

#print RecentLeastSquares('/home/elizabeth/Dropbox/Windows-LinuxShare/','PoudreStructures.csv')
