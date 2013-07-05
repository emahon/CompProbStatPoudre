#Elizabeth Mahon
#Read output files from waterbase mass exporter

import csv

def StructureReader(folder,read,write):
    i = 0
    prevnum = 0

    data = csv.reader(open((folder+read),'rb'), delimiter=',', quotechar='|')
    output = csv.writer(open((folder+write),'wb'),delimiter=',',quotechar='|')
    for row in data:
        if (row[8] != 'Well' and row[8] != 'Wellfield' and row[8] !='Well Field' and row[8] != 'Minimum Flow' and row[4] != 'N' and row[4] != 'F' and row[4] !='D' and 'POUDRE' in row[21] and row[3] != prevnum):
            output.writerow([row[3],row[4],row[5],row[8],row[38],row[39]])
            prevnum = row[3]

StructureReader('/home/elizabeth/Dropbox/Windows-LinuxShare/','120910_Structures.csv','AllPoudre.csv')
