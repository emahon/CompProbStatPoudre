#Elizabeth Mahon
#Computational Probability and Statistics
#Read streamflow documents and output as a dictionary

def FlowReader(flowfile):
    import csv

    flow = dict()

    #read streamflow data
    flowdata = csv.reader(open(flowfile,'rb'),delimiter=',',quotechar='|')
    for row in flowdata:
        flow[row[0]] = row[1]
    flow["2011-10"] = 0 #data only goes until Sept 2011
    flow["2011-11"] = 0 #but diversions go until Dec 2011
    flow["2011-12"] = 0 #Add the last ones manually to prevent size conflicts

    return flow
