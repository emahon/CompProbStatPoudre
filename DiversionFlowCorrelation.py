#Elizabeth Mahon
#Calculate the covariance between flows in the Poudre and diversions

from Covariance import Covariance
import correlation
from RecordReader import RecordReader
from FlowReader import FlowReader
import math

def DivFlowCorrelation():
    folder = '/home/elizabeth/Dropbox/Windows-LinuxShare/'
    master = 'PercentStructures.csv'
    diversions = list()
    yearflow = list()
    diffdiv = 0
    diffflow = 0
    rec_diffdiv = 0
    rec_diffflow = 0

    for i in range(62):
        diversions.append(0)
        yearflow.append(0)

    data = RecordReader(folder, master)
    flow = FlowReader((folder+'PoudreFlow.csv'))

    for i in range(62):
        for j in range(12):
            yearflow[i] += float(flow[(str(i+1950)+'-'+('{0:{fill}2}'.format(j+1,fill='0')))])
            #next part necessary because there's a bit of imprecision introduced in the indexes somewhere, so I can't just recalculate them
            for thing in data.keys():
                if(thing < (i+1950+.01*(j+1)+.005) and thing > (i+1950+.01*(j+1)-.005)):
                    diversions[i] += data[thing]

    #remove 1983 (huge outlier - super wet year!)
    yearflow.pop(33)
    diversions.pop(33)

    cov = Covariance(zip(yearflow, diversions))

    for i in range(len(yearflow)):
        diffdiv += (diversions[i] - (sum(diversions)/len(diversions)))**2
        diffflow += (yearflow[i] - (sum(yearflow)/len(yearflow)))**2

    dev_div = math.sqrt((1.0/len(diversions))*diffdiv)
    dev_flow = math.sqrt((1.0/len(yearflow))*diffflow)

    return cov/(dev_div*dev_flow), correlation.Corr(yearflow, diversions)

print DivFlowCorrelation()
