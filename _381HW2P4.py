import numpy as np
import sys

#p0=0.6;   e0=0.05;   e1=0.03

def message(p):
    if (np.sum(p) != 1.0):
        sys.exit("Total probability is not 1!")
    arrsum = np.cumsum(p)
    cp = np.append(0, arrsum)
    k = len(p)
    r = np.random.random()
    for i in range(0, k):
        if r > cp[i] and r <= cp[i+1]:
            d = i
            if(d == 0):
                return '000'
            else:
                return '111'

def error(p):
    arr = np.copy(p)
    for i in range(0, len(arr)):
        if (arr[i] == '000'):
            for j in range(len(arr[i])):
                r = np.random.random()
                if (r <= 0.05):
                    arr[i] = arr[i][:j] + '1' + arr[i][j+1:]          
        if (arr[i] == '111'):
            for j in range(len(arr[i])):
                r = np.random.random()
                if (r <= 0.03):
                    arr[i] = arr[i][:j] + '0' + arr[i][j+1:]
    return arr

def errorCheck(p):
    arr = np.copy(p)
    for i in range(0, len(arr)):
        ones = 0
        zero = 0
        for j in range(0, len(arr[i])):
            if(arr[i][j] == '0'):
                zero += 1
            if(arr[i][j] == '1'):
                ones += 1
        if(zero > ones):
            arr[i] = '000'
        else:
            arr[i] = '111'
    return arr

def main():
    prob = np.array([0.6, 0.4])
    sArr = np.array([])
    counter = 0
    for i in range(0, 100000):
        s = message(prob)
        sArr = np.append(sArr, s)
    rArr = error(sArr)
    eArr = errorCheck(rArr)
    for i in range(0, len(sArr)):
        if (sArr[i] == eArr[i]):
            counter += 1
    print('Prob: ', counter/100000)

main()