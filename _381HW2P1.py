import numpy as np
import sys

#p0=0.6;   e0=0.05;   e1=0.03

def message(arr):
    if (np.sum(arr) != 1.0):
        sys.exit("Total probability is not 1!")
    arrsum = np.cumsum(arr)
    cp = np.append(0, arrsum)
    k = len(arr)
    r = np.random.random()
    for i in range(0, k):
        if r > cp[i] and r <= cp[i+1]:
            d = i
            return d

def error(p):
    arr = np.copy(p)
    for i in range(0, len(arr)):
        if (arr[i] == 0):
            r = np.random.random()
            if (r <= 0.05):
                arr[i] = 1
        if (arr[i] == 1):
            r = np.random.random()
            if (r <= 0.03):
                arr[i] = 0
    return arr

def main():
    prob = np.array([0.6, 0.4])
    sArr = np.array([])
    counter = 0
    for i in range(0, 100000):
        s = message(prob)
        sArr = np.append(sArr, s)
    rArr = error(sArr)
    for i in range(0, len(sArr)):
        if (sArr[i] == rArr[i]):
            counter += 1
    print('Prob: ', counter/100000)

main()