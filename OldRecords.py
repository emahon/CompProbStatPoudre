#Elizabeth Mahon
#Read data only from structures that have data for the entire period
#1950-2011
#Use as a control for possible dataset anomalies

import csv

def OldRecords(folder, master):
    n = 0
    months = {'jan':.01,'feb':.02,'mar':.03,'apr':.04,'may':.05,'jun':.06,'jul':.07,'aug':.08,'sep':.09,'oct':.1,'nov':.11,'dec':.12}
    data = dict()

    #make structure to dump structure data into
    for q in range(62): #years
        for j in range(13): #months
            data[q+1950+j*.01] = 0

    #read structure diversion data
    masterdata = csv.reader(open((folder+master),'rb'),delimiter=',',quotechar='|')
    for row in masterdata:
        if (n > 0 and row[5].strip('"') == '1950' and row[6].strip('"') == '2011'):
            datafile = folder+str(row[0])+'.csv' #construct structure data name
            try:
                records = csv.reader(open(datafile,'rb'),delimiter=',',quotechar='|')
                for row in records:
                    if ('AF' in row[6]): #ensure measurement is in acre-feet
                        try:
                            x = float(row[7].strip('"'))
                        except ValueError:
                            x = 0
                        data[(int(row[4].strip('"'))+months[row[5].strip('"')])] += x #add measurement
            except IOError:
                pass
        n += 1

    return data

