#Elizabeth Mahon
#Trying to figure out how well the previous year(s) predict the next year(s)
#Calculates R^2 for structures....

import csv
import RSquared
import Cdf
from RecentLeastSquares import LeastSquares
import matplotlib.pyplot as pyplot

def prediction(folder, master):
    data = list()

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
                        if (int(row[4].strip('"')) not in temp.keys()):
                            temp[int(row[4].strip('"'))] = 0.0
                        else:
                            temp[int(row[4].strip('"'))] += x
                    except ValueError:
                        x = 0   
            #now that we have all the diversions from that structure, let's start making predictions
            if len(temp) > 1: #can't make predictions if we only have one year of data
                slope, intercept = LeastSquares(zip(temp.keys(), temp.values()))
                blah = list()
                for val in temp.keys():
                    blah.append(val*slope + intercept)
                data.append(RSquared.Rsquared(blah,temp.values()))
        except IOError:
            pass

    print data
    cdf = Cdf.MakeCdfFromList(data)
    x,y = cdf.Render()
    pyplot.plot(x,y)
    pyplot.xlim(-.01, 1.01)
    pyplot.title("How Well Previous Data Predicts New Diversions",fontsize=20)
    pyplot.xlabel("Percentage of Structures at or below Value", fontsize = 15)
    pyplot.ylabel("Coefficient of Determination for Linear Fit", fontsize = 15)
    pyplot.show()

prediction('/home/elizabeth/Dropbox/Windows-LinuxShare/','PercentStructures.csv')
