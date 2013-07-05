#Elizabeth Mahon
#Creating a probability mass function for structure sizes
#????

import csv
import numpy
import Pmf
import matplotlib.pyplot as pyplot

def StructurePMF(folder, master):

    sizes = list()
    data = dict()

    masterdata = csv.reader(open((folder+master),'rb'),delimiter=',',quotechar='|')
    for row in masterdata:
        datafile = folder+str(row[0])+'.csv' #construct structure data name
        temp = dict()
        try:
            records = csv.reader(open(datafile,'rb'),delimiter=',',quotechar='|')
            for row in records:
                if ('AF' in row[6]): #ensure measurement is in acre-feet
                    try:
                        x = float(row[7].strip('"'))
                        if (row[4].strip('"') not in temp.keys()):
                           temp[row[4].strip('"')] = 0
                        else:
                           temp[row[4].strip('"')] += x
                    except ValueError:
                        x = 0
            try:
                sizes.append(max(temp.values()))
            except ValueError:
                pass
        except IOError:
            pass

    keys = numpy.linspace(0,max(sizes),10)
    for i in range(len(keys) - 1):
        data[keys[i+1]] = 0
        for item in sizes:
            if item > keys[i] and item <= keys[i+1]:
                data[keys[i+1]] += 1

    print data

    PMF = Pmf.MakePmfFromDict(data)
    PMF.Normalize()
    x,y = PMF.Render()

    pyplot.bar(x,y)
    pyplot.xlabel("Structure Capacity (AF)",fontsize=15)
    pyplot.ylabel("Probabilty of Capacity Smaller than or Equal to Value",fontsize=15)
    pyplot.title("Probabilty Mass Function of Structure Capacity",fontsize=20)
    pyplot.show()

StructurePMF('/home/elizabeth/Dropbox/elizabeth.mahon/Data/','PercentStructures.csv')
