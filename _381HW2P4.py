import numpy as np
import sys

#p0=0.6;   e0=0.05;   e1=0.03

#creates a random number string based off of a given probability
def message(p):
    #exits if the total probability is not 1
    if (np.sum(p) != 1.0):
        sys.exit("Total probability is not 1!")
    arrsum = np.cumsum(p) #creates a cumulative sum with the probability
    cp = np.append(0, arrsum) #appends a 0 to the front of the cumulative prob array
    k = len(p) #stores the length of the argument array
    r = np.random.random() #creates a random number between 0 and 1
    #returns a random string 000 or 111 based on the probability
    for i in range(0, k):
        if r > cp[i] and r <= cp[i+1]:
            d = i
            if(d == 0):
                return '000'
            else:
                return '111'
    return -1

#creates errors in the sent messages based on probability
def error(p):
    arr = np.copy(p) #creates a copy of the array to avoid editting the original
    #loops through the array to create error
    for i in range(0, len(arr)):
        #potentially changes one or more zeros to ones
        if (arr[i] == '000'):
            for j in range(len(arr[i])):
                r = np.random.random()
                if (r <= 0.05):
                    arr[i] = arr[i][:j] + '1' + arr[i][j+1:]      
        #potentially changes one or more ones to zeros    
        if (arr[i] == '111'):
            for j in range(len(arr[i])):
                r = np.random.random()
                if (r <= 0.03):
                    arr[i] = arr[i][:j] + '0' + arr[i][j+1:]
    return arr

#function which aims to 'fix' error in the recieved messages
def errorCheck(p):
    arr = np.copy(p) #creates a copy of user supplied array
    #loops through the array to fix erroneous messaged
    for i in range(0, len(arr)):
        ones = 0 #counts the number of ones in an array
        zero = 0 #counts the number of zeros in an array
        #loops through a single message and determines the number of 1s and 0s
        for j in range(0, len(arr[i])):
            if(arr[i][j] == '0'):
                zero += 1
            if(arr[i][j] == '1'):
                ones += 1
        #sets the message to 000 if there were more 0s
        if(zero > ones):
            arr[i] = '000'
        #sets the message to 111 if there were more 1s
        else:
            arr[i] = '111'
    return arr

def main():
    prob = np.array([0.6, 0.4]) #an array to store porbabilities
    sArr = np.array([]) #an array to store sent messages
    counter = 0 #an array to count the number of times a sent message id the same
                #as the recieved one
    #creates 100000 messages
    for i in range(0, 100000):
        s = message(prob)
        sArr = np.append(sArr, s)
    rArr = error(sArr) #adds errors to the sent messages
    eArr = errorCheck(rArr) #attempts to repair erroneous messages
    #loops through the array and counts the number of correctly recieved messages
    for i in range(0, len(sArr)):
        if (sArr[i] == eArr[i]):
            counter += 1
    print('Prob: ', counter/100000)

main()