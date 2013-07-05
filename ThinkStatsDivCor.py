from RecordReader import RecordReader
from FlowReader import FlowReader
import correlation

def DivFlowCorrelation():
    folder = '/home/elizabeth/Dropbox/Windows-LinuxShare/'
    master = 'PoudreStructures.csv'
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

    print correlation.Corr(yearflow, diversions)

    print correlation.Corr(yearflow[52:60],diversions[52:60])

DivFlowCorrelation()
