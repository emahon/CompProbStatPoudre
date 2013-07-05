#Elizabeth Mahon
#Build a CDF of diversion sizes in any given year to determine if there's a good model

import csv
import Cdf
import matplotlib.pyplot as pyplot
import math
from RecentLeastSquares import LeastSquares
import erf
import thinkstats

def CumulativeStructures(folder, master):

    alldata = list()
    expon = list()
#    expon2 = list()
    expon3 = list()
    blah = list()
    pareto1 = list()
    logx = list()
    logy = list()
    pareto2 = list()

    for file in master:
        data = list()
        masterdata = csv.reader(open((folder+file),'rb'),delimiter=',',quotechar='|')
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
                    data.append(max(temp.values()))
                except ValueError:
                    pass
            except IOError:
                pass
        alldata.append(data)

    cdf = Cdf.MakeCdfFromList(alldata[0])
    x, y = cdf.Render()

    #estimate an exponential curve, using 1/lambda ~= mean
    mean = float(sum(x)/len(x))
    for val in x:
        expon.append(1-(math.exp(-val*(1.0/mean))))

    #estimate an exponential curve using var = 1/lambda^2
    var = thinkstats.Var(x)
    for val in x:
        expon3.append(1-math.exp(-val*math.sqrt(1.0/var)))

    #bad approximation - left here so I know what failed
    #estimate an exponential curve using log(1-CDF) = -lambda x
    #for val in y:
    #    if val != 1:
    #        blah.append(math.log(1-val))
    #    else:
    #        blah.append(0) #keep x and new y same size; might be an issue.
    #lamb, zero = LeastSquares(zip(x,blah))
    #for val in x:
    #    expon2.append(1-(math.exp(lamb*val)))

    #bad approximation
    #estimate a pareto curve
    #based on http://www.math.umt.edu/gideon/pareto.pdf
    #breaks down if min(x) = 0
    #a = float((len(x)*mean - min(x))/(len(x)*(mean - min(x))))
    #m = float((len(x)*a - 1)*min(x)/(len(x)*a))
    #print a, m
    #for val in x:
    #    pareto1.append(1 - (val/m)**-a)

    #estimate a pareto curve
    #based on slope of loglog plot
    for i in range(len(x)):
        if y[i] != 1 and x[i] != 0:
            logy.append(math.log(1 - y[i]))
            logx.append(math.log(x[i]))
    alpha, alpham = LeastSquares(zip(logx,logy))
    print alpha, alpham
    km = math.exp(alpham/alpha)
    for val in x:
        pareto2.append(1-(val/km)**alpha)

    #estimate a lognormal curve
    logmean = sum(logx)/len(logx)
    logdev = math.sqrt(thinkstats.Var(logx))
    #cdf = erf.NormalCdf(logx[int(len(logx)/2)], mu = logmean, sigma = logdev)
    #lognormx, lognormy = cdf.Render()

    x2,y2 = (Cdf.MakeCdfFromList(alldata[1])).Render()
    
    pyplot.title("CDF of Maximum Diversions",fontsize=20)
    pyplot.xlabel("Diversions (AF)",fontsize=15)
    pyplot.ylabel("Fraction of Structures at or below Diversion Size",fontsize=15)
    pyplot.plot(x,y)
    pyplot.plot(x2,y2)
    pyplot.plot(x,expon)
#    pyplot.plot(x,expon2)
    pyplot.plot(x,expon3)
    #pyplot.plot(x,pareto1)
    pyplot.plot(x,pareto2)
#    pyplot.plot(lognormx, lognormy)
    pyplot.xlim(min(x),max(x))
    pyplot.legend(("Data","All Structures","Exponential Approximation lambda = "+str(round(-(1.0/mean),6)),"Exponential Approximation lambda = "+str(round(math.sqrt(1.0/var),6)),"Pareto Approximation alpha = "+str(round(alpha,2))+" km = "+str(round(km,2))),loc ='lower right')
    pyplot.show()

CumulativeStructures('/home/elizabeth/Dropbox/elizabeth.mahon/Data/',['PercentStructures.csv','PoudreStructures.csv'])
