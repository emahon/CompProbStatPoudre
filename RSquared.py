#Elizabeth Mahon
#Creating something that will calculate the R squared value

def Variance(guesses, vals):
    tot = 0.0
    for i in range(len(vals)):
        tot += ((guesses[i] - vals[i])**2)
    return float(tot/len(vals))

def Rsquared(guesses, values):
    means = list()
    mean = sum(values)/float(len(values))
    for i in range(len(values)):
        means.append(mean)
    g = Variance(guesses, values)
    v = Variance(means,values)
    if v != 0:
        return (1 - g/v)
    else:
        return 1 #perfect correlation
