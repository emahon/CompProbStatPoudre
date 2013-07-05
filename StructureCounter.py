#Elizabeth Mahon
#Computational Probability and Statistics
#Count the number of structures diverting water per year

import csv

def StructureCounter(folder, master):
    data = dict()
    year = 0
    n = 0
    m = 0

    for q in range(62):
        data[q+1950] = 0

    #read structure data
    masterdata = csv.reader(open((folder+master),'rb'),delimiter=',',quotechar='|')
    for row in masterdata:
        if n > 0:
            datafile = folder+str(row[0])+'.csv' #construct structure data name
            try:
                records = csv.reader(open(datafile,'rb'),delimiter=',',quotechar='|')
                for r in records:
                    if (r[4].strip('"') != year and m > 0): #if a new year....
                        year = r[4].strip('"')
                        data[int(year)] += 1 #increment # of structures that year
                    m += 1
                m = 0
            except IOError:
                pass
        n += 1

    return data
