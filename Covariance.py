#Elizabeth Mahon
#Calculates covariance
#Takes a list of tuples (x,y), outputs covariance

def Covariance(values):
    x, y = zip(*values)

    mean_x = sum(x)/float(len(x))
    mean_y = sum(y)/float(len(y))

    prod = 0
    for i in range(len(x)):
        prod += (x[i] - mean_x)*(y[i] - mean_y)

    return prod/len(x)
