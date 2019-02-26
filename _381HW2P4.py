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

#creates errors in the sent messages based on probability
def error(s):
    if(s == 0):
        r = np.random.random()
        if (r <= 0.05):
            return 1      
        #potentially changes one or more ones to zeros    
    if (s == 1):
        r = np.random.random()
        if (r <= 0.03):
            return 0
    return s

def main():
    prob = np.array([0.6, 0.4]) #an array to store porbabilities
    counter = 0 #an array to count the number of times a sent message id the same
                #as the recieved one
    #creates 100000 messages
    for i in range(0, 100000):
        s = message(prob)
        zeros = 0
        ones = 0
        for j in range(0, 3):
            r = error(s)
            if (r == 0):
                zeros += 1
            elif (r == 1):
                ones += 1
        if (zeros > ones and s == 0):
            counter += 1
        elif (ones > zeros and s == 1):
            counter += 1
    
        
    print('Prob: ', counter/100000)

main()