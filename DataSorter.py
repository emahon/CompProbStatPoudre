#Elizabeth Mahon
#Determine percentage of years structure has existed that it has reported data for
#Create a spreadsheet listing structures with good data
#Graph the CDF of the fraction of years each structure reports for

import csv
import Cdf
import matplotlib.pyplot as pyplot
import numpy as np

class structure:
    first_year = 0
    last_year = 0
    num_recorded = 0
    def __init__(self, name):
        self.name = name
    def set_firstyear(self, year):
        self.first_year = year
    def set_lastyear(self, year):
        self.last_year = year
    def tot_recorded(self, num_recorded):
        self.num_recorded = num_recorded
    def num_increment(self):
        self.num_recorded += 1

def DataSorter(folder, master, write):
    structdata = dict()
    fileadds = ['-release','-storage','-comments',''] #different record types
    locations = [4, 11, 4, 4] #where the year is stored in each record type
    n = 0

    #read files
    masterdata = csv.reader(open((folder+master),'rb'),delimiter=',',quotechar='|')
    for row in masterdata:
        structdata[row[0]] = structure(row[2])
        #run through records and record first and last years
        for i in range(len(fileadds)):
            suffix = fileadds[i]
            sel = locations[i]
            filename = folder+str(row[0])+suffix+'.csv'
            try:
                records = csv.reader(open(filename,'rb'),delimiter=',',quotechar='|')
                for row2 in records:
                    try:
                        year1 = structdata[row[0]].first_year
                        curyear = int(row2[sel].strip('"'))
                        if (year1 == 0 or curyear < year1): #update first year
                            structdata[row[0]].set_firstyear(curyear)
                        if (structdata[row[0]].last_year < curyear): #update last year
                            structdata[row[0]].set_lastyear(curyear)
                        if suffix == '': #count number of years with recorded data when we get to diversion records
                            structdata[row[0]].num_increment()
                    except ValueError: #ignore errors if trying to cast a non-number to an int
                        pass
            except IOError: #don't worry if the file doesn't exist
                pass

    #write to output file
    keys = structdata.keys()
    data = structdata.values()
    graphdata = list()
    output = csv.writer(open((folder+write),'wb'),delimiter=',',quotechar='|')
    for n in range(len(keys)):
        if (data[n].num_recorded == 0):
            frac = 0
        else:
            frac = float(data[n].num_recorded/12)/(float(data[n].last_year - data[n].first_year) + 1) #Get what fraction of years it reports
        graphdata.append(frac*100)
        if frac > .9: #record structures that report more than 90% of years
            output.writerow([keys[n],data[n].name, data[n].first_year, data[n].last_year, data[n].num_recorded,frac])

    #plot
    cdf = Cdf.MakeCdfFromList(graphdata)
    x, y = cdf.Render()
    pyplot.plot(x,y)
    pyplot.xlim(-1, 101)
    pyplot.title("Reliability of Structure Data",fontsize=20)
    pyplot.xlabel("% of years reported", fontsize=15)
    pyplot.ylabel("Fraction of structures at or below level", fontsize=15)
    pyplot.show()

#My attempt at graphing the cdf
#    freq = list()
#    n = 0.0
#    for item in graphdata:
#        n += 1
#        freq.append(n/len(graphdata))
#
#    print graphdata
#    print freq
#    pyplot.plot(graphdata, freq)
#    pyplot.show()

DataSorter('/home/elizabeth/Dropbox/Data/','PoudreStructures.csv','PercentStructures.csv')
