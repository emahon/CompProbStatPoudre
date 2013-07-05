#Elizabeth Mahon
#Reading all the individual diversion structure data given a
#spreadsheet with master data

import csv
import matplotlib.pyplot as pyplot
import numpy as np
from OldRecords import OldRecords
from FlowReader import FlowReader
from RecordReader import RecordReader

def YearlyGrapher(master, folder, flowfile,complete,div):

    months = {'jan':.01,'feb':.02,'mar':.03,'apr':.04,'may':.05,'jun':.06,'jul':.07,'aug':.08,'sep':.09,'oct':.1,'nov':.11,'dec':.12}

    if complete=='o':
        data = OldRecords(folder, master)
    else:
        data = RecordReader(folder, master)
    flow = FlowReader(folder+flowfile)

    #graphing
    #initialize variables for graph
    labels = list()
    width = .1
    dates = data.keys()
    dates.sort()
    olddiversions = list()
    oldflow = list()
   
    for q in range(62): #initialize olddiversions so it can be used to set the bottom
        olddiversions.append(0)

    ind  = np.arange(len(olddiversions))

    for j in range(12): #loop through all months
        diversions = list() #clear old list
        for date in dates: #make columns for each year instead of each month
            if (((date - int(date)) < ((j+1)*.01 + .005)) and ((date - int(date)) > ((j+1)*.01 - .005))):
                diversions.append(data[date])
                if j == 11:
                    labels.append(int(date)) #create x labels on last month

        pyplot.bar(ind, diversions, bottom = olddiversions, color=str((j+int(1))/12.0))
        for s in range(len(olddiversions)):
            olddiversions[s] = olddiversions[s] + diversions[s] #get diversions for year to date

    if div == 'y':
        #get plot data for streamflow
        for q in range(62): #initialize old flow to serve as bottom
            oldflow.append(0)
        for j in range(12):
            monflow = list() #clear old list
            for i in range(62):
                monflow.append(float(flow[str(i+1950)+'-'+('{0:{fill}2}'.format(j+1,fill='0'))]))
            pyplot.bar(ind, monflow, bottom = oldflow, color =(0,0,(j+1)/12.0), alpha = .5)
            for s in range(len(oldflow)):
                oldflow[s] = oldflow[s] + monflow[s]

    #get months in order
    monlabels = list()
    mon = months.values()
    mon.sort()
    for m in mon:
        for k in months:
            if months[k] == m:
                monlabels.append(k)
    
    pyplot.xticks(ind+width,labels,rotation='vertical')
    pyplot.xlabel("Year",fontsize="15")
    pyplot.ylabel("Diversions in Acre-Feet",fontsize="15")
    pyplot.legend(monlabels)
    pyplot.title("Diversions over Time",fontsize="20")
    pyplot.show()

YearlyGrapher('PercentStructures.csv','/home/elizabeth/Dropbox/Data/','PoudreFlow.csv','n','n')
