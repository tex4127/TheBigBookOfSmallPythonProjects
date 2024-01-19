# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 09:49:25 2024

This source code file is related to the solving of the following project:
    
Book:           The Big Book of Small Python Projects
Project #:      2
Project Title:  Birthday Paradox

Description:
    This is to be a game where the computer generates a user input number of 
    birthday values (i.e Oct 9) and performs monte carlo sims to determine the
    percentage of overlapping birthdays for a set number of iterations

The main difference to this approach is that we want to play with multithreading.
The c++ version of this will also do multithreading to decrease time to complete

@author: Jacob Garner
"""


''' DEPENDANCIES '''
import time
import random
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import csv
from csv import writer
import threading

''' CONTROL & CONFIG VARIABLES '''

numberSims = 100000

''' FUNCTIONS '''

def generateBirthdays(n_g):
    birthdays = []
    for i in range(n_g):
        birthdays.append(time.strftime("%b %d", time.localtime(random.randint(0, 1.262*10**8))))
    return birthdays
     
def compareBirthdays(birthdays):
    for i in range(len(birthdays)):
        c = birthdays.count(birthdays[i])
        if c > 1:
            return 1
    return 0
  
def runSim(numBirth, numSims, results, index):
    prob = 0
    for i in range(numSims):
        if i % 10000 == 0:
            print("Running Simulation {:d}".format(i))
        b_list = generateBirthdays(int(numBirth))
        prob += compareBirthdays(b_list)
        
    print('Thread {:d} Results: '.format(index), prob/numberSims)
    results[index] = prob/numberSims
    return prob/numberSims
    
#next we need to request a number of birthdays from the user 
numBirthdays = input("How many Birthdays should be generated?\n")
numThreads = 1
try:
    numThreads = int(input("On how many threads would you like to run? (max of 4) \n"))
    if numThreads < 1 or numThreads > 4:
        numThreads = 1
except:
    print("Value not understood or out of range. Switching to single thread Mode")
print("Now Generating {:d} Generations of birthdays.".format(numberSims))
input("Press 'Enter' to begin simulations.")

#we need a list to index our threads
threads = [None] * numThreads
#we need a list to index our results
results = [None] * numThreads

for i in range(numThreads):
    threads[i] = threading.Thread(target=runSim, args = (numBirthdays, numberSims//numThreads, results, i))
    threads[i].start()

for i in range(numThreads):
    threads[i].join()
    

while 1:
    deadThreads = 0
    for i in range(numThreads):
        if not(threads[i].is_alive()):
            deadThreads += 1
    if deadThreads == numThreads :
        break;


#get the average of the results
totalProb = sum(results)

print(totalProb)
