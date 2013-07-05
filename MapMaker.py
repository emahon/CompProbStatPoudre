#Elizabeth Mahon
#Output a CSV of locations to map using Google's Fusion Table

import csv
import LatLongUTMconversion as conv

def MapMaker(folder, master, good_data, with_data, no_data, write):
    masterdata = list(csv.reader(open((folder+master),'rb'),delimiter=',',quotechar='|')) #need to do this to iterate over it multiple times
    structdata = csv.reader(open((folder+with_data),'rb'),delimiter=',',quotechar='|')
    structnone = csv.reader(open((folder+no_data),'rb'),delimiter=',',quotechar='|')
    structgood = csv.reader(open((folder+good_data),'rb'),delimiter=',',quotechar='|')

    output = csv.writer(open((folder+write),'wb'),delimiter=',',quotechar='|')
    has_data = list()

    for row in structgood:
        has_data.append(str(row[0]))
        for row2 in masterdata:
            if (str(row[0]) == str(row2[3])):
                try:
                    Lat,Long = conv.UTMtoLL(11,float(row2[10]),float(row2[9]),'13N')
                    output.writerow([row[0],row[2],Lat,Long,2])
                except ValueError:
                    pass

    for row in structdata:
        has_data.append(str(row[0]))
        for row2 in masterdata:
            if (str(row[0]) == str(row2[3]))  and not (str(row[0]) in has_data):
                try:
                    Lat,Long = conv.UTMtoLL(11,float(row2[10]),float(row2[9]),'13N')
                    output.writerow([row[0],row[2],Lat,Long,1])
                except ValueError:
                    pass

    for row in structnone:
        for row2 in masterdata:
            if (str(row[0]) == str(row2[3])) and not (str(row[0]) in has_data):
                try:
                    Lat,Long = conv.UTMtoLL(11,float(row2[10]),float(row2[9]),'13N')
                    output.writerow([row[0],row[2],Lat,Long,0])
                except ValueError:
                    pass

MapMaker('/home/elizabeth/Dropbox/Data/','120910_Structures.csv','PercentStructures.csv','PoudreStructures.csv','AllPoudre.csv','Map.csv')
