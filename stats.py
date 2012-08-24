
def var( n ):
    average = mean(n)
    abs_deviation = [ (x-average)**2 for x in n]
    return mean(abs_deviation)

def mean( n ):
    return sum(n)/len(n)

def sd(n):
    return var(n) ** .5



if __name__ == '__main__':
    filename = "sample_data_set.txt"
    with open(filename) as f:
        data = [float(line) for line in f]

    print mean(data)
    print var(data)
    print sd(data)


