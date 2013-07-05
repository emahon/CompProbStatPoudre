#Elizabeth Mahon
#Computational Probability and Statistics
#Plot the mean diversion per structure per year

def AverageGrapher(folder, master):
    import matplotlib.pyplot as pyplot
    import numpy as np
    from RecordReader import RecordReader
    from StructureCounter import StructureCounter

    structures = StructureCounter(folder, master)
    data = RecordReader(folder, master)

    diversions = list()
    struct = list()
    averages = list()
    labels = list()

    for q in range(62):
        diversions.append(0)
        struct.append(0)

    for i in range(62):
        struct[i] += structures[1950+i]
        for j in range(12):
            diversions[i] += data[1950+i+(j+1)*.01]

    for q in range(62):
        averages.append(diversions[q]/struct[q])
        labels.append(q+1950)

    ind = np.arange(62)

    pyplot.bar(ind, averages)
    pyplot.xticks(ind+.5, labels, rotation='vertical')
    pyplot.xlabel("Year",fontsize='15')
    pyplot.ylabel("Mean Diversion in Acre-Feet",fontsize='15')
    pyplot.title("Mean Diversions over Time",fontsize='20')
    pyplot.show()

AverageGrapher('/home/elizabeth/Dropbox/Windows-LinuxShare/','PoudreStructures.csv')
