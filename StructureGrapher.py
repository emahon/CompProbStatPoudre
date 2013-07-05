#Elizabeth Mahon
#Computational Probability and Statistics
#Graph the counted number of structures

import matplotlib.pyplot as pyplot
import numpy as np
from StructureCounter import StructureCounter

def StructureGrapher(folder, master):
    data = StructureCounter(folder, master)
    width = .1
    things = data.items()
    things.sort()
    dates = list()
    values = list()

    for date, value in things:
        dates.append(date)
        values.append(value)

    ind = np.arange(len(dates))

    pyplot.plot(ind,values)
    pyplot.xticks(ind+width,dates,rotation='vertical')
    pyplot.xlabel("Year",fontsize="15")
    pyplot.ylabel("# of structures reporting data",fontsize="15")
    pyplot.title("# of Structures over Time",fontsize="20")
    pyplot.show()


StructureGrapher('/home/elizabeth/Dropbox/Windows-LinuxShare/','PoudreStructures.csv')
