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
  
def runSim(numBirth, numSims):
    prob = 0
    for i in range(numSims):
        if i % 10000 == 0:
            print("Running Simulation {:d}".format(i))
        b_list = generateBirthdays(int(numBirth))
        prob += compareBirthdays(b_list)
        
    print(prob/numberSims)
    return prob/numberSims
    
def plotFullSweep():
    x = []
    y = []
    plot50 = True
    plot75 = True
    plot90 = True
    plot95 = True
    figure = plt.figure(figsize=(8,5))
    for i in range(2,80):
        print("Simulating Group Size: {:d}".format(i))
        y.append(runSim(i, numberSims))
        x.append(i)
        if plot50 and y[-1] >= 0.5:
            plt.plot([i-3, i+3], [y[-1], y[-1]], color = 'cyan', label = '50% Chance @ {:d} People'.format(i), linewidth = 1)
            plt.plot([i, i], [y[-1]-0.05, y[-1]+0.05], color = 'cyan', linewidth = 1)
            plot50 = False
        if plot75 and y[-1] >= 0.75:
            plt.plot([i-3, i+3], [y[-1], y[-1]], color = 'chocolate', label = '75% Chance @ {:d} People'.format(i), linewidth = 1)
            plt.plot([i, i], [y[-1]-0.05, y[-1]+0.05], color = 'chocolate', linewidth = 2)
            plot75 = False
        if plot90 and y[-1] >= 0.90:
            plt.plot([i-3, i+3], [y[-1], y[-1]], color = 'chartreuse', label = '90% Chance @ {:d} People'.format(i), linewidth = 1)
            plt.plot([i, i], [y[-1]-0.05, y[-1]+0.05], color = 'chartreuse', linewidth = 1)
            plot90 = False
        if plot95 and y[-1] >= 0.95:
            plt.plot([i-3, i+3], [y[-1], y[-1]], color = 'black', label = '95% Chance @ {:d} People'.format(i), linewidth = 1)
            plt.plot([i, i], [y[-1]-0.05, y[-1]+0.05], color = 'black', linewidth = 1)
            plot95 = False
    plt.title("Percent Chance of at Least 2 People Having the Same Birthday \n for Various Group Sizes (100000 Simulations)", fontsize = 16)
    plt.xlabel("Size of Group (# of People)")
    plt.ylabel("Percent Chance of Similar Birthday")
    plt.scatter(x, y, color = 'darkmagenta', s = 2)
    plt.grid(True)
    plt.legend(loc='lower right')
    plt.savefig('FullSweepData_BirthdayParadox.png')
    #for me, lets also save this data to 
    df_data = pd.DataFrame({'GroupSize' : x,
                           'PercentSimilarBirthday' : y})
    df_data.to_csv('FullSweepData_BirthdayParadox.csv')

''' MAIN PROGRAM '''
    
    
#next we need to request a number of birthdays from the user 
numBirthdays = input("How many Birthdays should be generated?\n")

print("Now Generating {:d} Generations of birthdays.".format(numberSims))
input("Press 'Enter' to begin simulations.")

runSim(numBirthdays, numberSims)
plotData = input('Would you like to plot all values for Birthday Paradox Monte Carlo Sims for groups of people between 2 and 100? y/n \n')
if 'y' in plotData:
    plotFullSweep()

