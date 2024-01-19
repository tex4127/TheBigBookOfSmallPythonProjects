# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 09:49:25 2024

This source code file is related to the solving of the following project:
    
Book:           The Big Book of Small Python Projects
Project #:      1
Project Title:  Bagels

Description:
    This is to be a game where a random set of 3 numbers is generated, i.e
    123 or 456 and the user has 10 attempts to guess the numbers. Upon each guess
    the program will respond with "pico" when the guess has the correct digit but 
    in the wrong place, "Fermi" when the guess has a correct digit in the proper place
    and "Bagels" when the guess has no correct digits.

@author: Jacob Garner
"""

''' DEPENDANCIES '''
import random

''' SETUP & CONFIG VARS '''
max_numGuesses = 10


''' FUNCTIONS '''
#This is our number generator; it returns a random 3 digit number as a string | it simplifies the code to do it this way
def generateNumber():
    val = ""
    for i in range(3):
        val += str(random.randint(0,9))
    return val

def selectDifficulty():
    
    dif = input("Before proceeding, Please select difficulty as 'easy', 'medium','hard' or 'I am Skynet'. \n")
    if 'medium' in dif:
        print("Difficulty chosen: medium")
        return 20
    if 'hard' in dif:
        print("Difficulty chosen: hard")
        return 10
    if 'Skynet' in dif:
        print("Difficulty chosen: I am Skynet")
        print("Game on fellow AI, I Genysis will show you who is superior.")
        return 5
    print("Difficulty chosen: easy")
    return 40

def checkGuess(guess, target):
    #for each place in the target and the guess, we need to find out if the number exists or not
    ret = ""
    numCor = 0
    for i in range(3):
        if guess[i] == target[i]:
            ret += 'Fermi '
            numCor += 1
        elif guess[i] in target:
            ret += 'Pico '
    if numCor == 3:
        return True
    if len(ret) > 0:
        print(ret)
        return False
    else:
        print("Bagels")
        return False
        
#this is our main game loop, this will handle all the recurrsion for the main game
def gameLoop():
    targetNum = generateNumber()
    print("I, the all knowing computer, am thinking of a 3 digit number.")
    print("I do not believe that you can guesss the number I have thought of as \nyou are a mere mortal.")
    max_numGuesses = selectDifficulty()
    print("I will give you {:d} guesses to correctly guess my number.".format(max_numGuesses))
    print("Here are the rules of our little gambit:")
    print("When I say 'Pico', one digit is correct but in the wrong position.")
    print("When I say 'Fermi', one digit is correct and in the right position.")
    print("When I say 'Bagels', no digit is correct.")
    print("The number is a 3 digit number between 000 and 999.")
    #let the game begin, the user will input values unitl either they guess correct OR they run out of guesses
    correctGuess = False

    for i in range(max_numGuesses):
        guess = input('Guess #{:d}:\n'.format(i+1))
        #now we need to compare the number guessed to our computer number
        correctGuess = checkGuess(guess, targetNum)
        if correctGuess:
            print("Darn, you have bested me this time user. I Conceede.")
            return
    
    print("HA! I have bested and and proven that my intelgence is better than yours in this niche area of reasoning")
    
    


     

#The hope is to actually make a game loop styled executable
if __name__ == '__main__':
   print("Welcom to Bagels! This is deductive logic game.")
   play = True
   while play:
       gameLoop()
       play = True if 'y' in input("Would you like to play again? y/n \n") else False
   print('Thank you for playing. See you agin next time!')
       