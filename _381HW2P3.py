import numpy as np
import sys

#p0=0.6;   e0=0.05;   e1=0.03

#creates a random message that is either 0 or 1 based on the
#array argument
def message(arr):
    #exits the program if the total probability is not 1
    if (np.sum(arr) != 1.0):
        sys.exit("Total probability is not 1!")
    arrsum = np.cumsum(arr) #converts the array into a cumulative sum array
    cp = np.append(0, arrsum) #appends a 0 to the front of the array
    k = len(arr) #gets the length of the array
    r = np.random.random() #gets a random number between 0 and 1
    #returns a number based on the random number and the probability array
    for i in range(0, k):
        if r > cp[i] and r <= cp[i+1]:
            d = i
            return d
    return -1

#creates errors in binary array
def error(p):
    arr = np.copy(p) #creates a copy of the array in order to avoid editting the original array
    #loops through the whole array and adds errors based on the probability of error
    for i in range(0, len(arr)):
        #if the number in the array is not binary, the program exits
        if (arr[i] != 1 or arr[i] != 0):
            sys.exit("Incorrect input!")
        #potentially replaces the current 0 with 1
        if (arr[i] == 0):
            r = np.random.random()
            if (r <= 0.05):
                arr[i] = 1
        #potentially replaces the current 1 with 0
        if (arr[i] == 1):
            r = np.random.random()
            if (r <= 0.03):
                arr[i] = 0
    return arr

def main():
    prob = np.array([0.6, 0.4]) #array to store the probabilty
    sArr = np.array([]) #array to store sent messages
    counter = 0 #counts the number of times 1 was correctly recieved
    sCounter = 0 #counts the number of times 1 was sent
    #creates a random array of sent messages
    for i in range(0, 100000):
        s = message(prob)
        sArr = np.append(sArr, s)
    rArr = error(sArr) #creates an erray of recieved messages with a
                       #potential for error
    #loops through the arrays and counts the number of times a 1 was 
    #recieved and a 1 was sent
    for i in range(0, len(sArr)):
        if (rArr[i] == 1):
            counter += 1
            if (sArr[i] == 1):
                sCounter += 1
    print('Prob: ', sCounter/counter)

main()