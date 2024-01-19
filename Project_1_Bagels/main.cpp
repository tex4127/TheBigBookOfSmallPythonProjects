/*
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
*/

#include<iostream>
#include<stdlib.h>
#include<time.h>
#include<string>
#include<stdint.h>

/*!
 *  @brief Simple enum to force specific types. Decided to go with a simpler std::string::find method instead since the program is simple.
 */
typedef enum
{
    easy,
    medium,
    hard,
    skynet
}difficulty_t;

/*!
 *  @brief Generates a reandom 3 digit number and returns this value as a string
 */
std::string generateNumber()
{
    std::string val = "";
    //before getting random numbers, lets seed our rand first
    //srand(time(NULL));
    for (uint8_t i = 0; i<3;i++)
    {
        //generate random number | use modulo to make sure its between 
        int num = rand()%10;
        val += std::to_string(num);
    }
    std::cout << val << std::endl;
    return val;
    
}

int selectDifficulty()
{
    std::cout << "Before proceeding, Please select difficulty as 'easy', 'medium','hard' or 'I am Skynet'." << std::endl;
    std::string dif;
    std::getline(std::cin, dif);
    //std::cout << dif <<std::endl;
    //Now check for the difficulty selected by the user
    if(dif.find("easy") != std::string::npos)
    {
        std::cout << "Difficulty Chosen: easy"<<std::endl;
        return 40;
    }
    else if(dif.find("medium")!= std::string::npos)
    {
        std::cout << "Difficulty Chosen: medium"<<std::endl;
        return 20;
    }
    else if(dif.find("hard")!= std::string::npos)
    {
        std::cout << "Difficulty Chosen: hard"<<std::endl;
        return 10;
    }
    else if(dif.find("Skynet")!= std::string::npos)
    {
        std::cout << "Difficulty Chosen: I am Skynet"<<std::endl;
        std::cout << "Game on fellow AI, I Genysis will show you who is superior." <<std::endl;
        return 5;
    }
    else
    {
        std::cout << "I did not understand your input. This must mean that you are bad at directions...\nAs a kindness, we will set the difficulty to easy." <<std::endl;
    }
    return 40;
}

int checkGuess(std::string g, std::string t)
{
    std::string ret ="";
    uint8_t numCor = 0;
    for (uint8_t i = 0; i < 3; i++)
    {
        char g_i = g[i];
        char t_i = t[i];
        if(g[i] == t[i])
        {
            numCor++;
            ret += "Fermi ";
        }
        else if(t.find(g[i])!= std::string::npos)
        {
            ret += "Pico ";
        }
    }
    if(numCor == 3)return 1;
    if(ret.size() > 1)
    {
        std::cout << ret<<std::endl;
    }
    else
    {
        std::cout <<"Bagels"<<std::endl;
    }
    return 0;
}

int gameLoop()
{
    std::cout << "I, the all knowing computer, am thinking of a 3 digit number." <<std::endl;
    std::cout << "I do not believe that you can guesss the number I have thought of as \nyou are a mere mortal." << std::endl;
    int max_numberGuesses = selectDifficulty();
    std::cout << "I will give you " << max_numberGuesses << " guesses to correctly guess my number." << std::endl;
    std::cout << "Here are the rules of our little gambit: " << std::endl;
    std::cout << "When I say 'Pico', one digit is correct but in the wrong position." << std::endl;
    std::cout << "When I say 'Fermi', one digit is correct and in the right position." << std::endl;
    std::cout << "When I say 'Bagels', no digit is correct." << std::endl;
    std::cout << "The number is a 3 digit number between 000 and 999." << std::endl;
    std::string targetNum = generateNumber();
    //int correctGuess = 0;
    for (uint8_t i = 0; i < max_numberGuesses; i++)
    {
        //read an input, then determine correctness of input relative to the generated number.
        std::cout << "Guess #: " << i+1 << " (of "<< max_numberGuesses << ")" <<std::endl;
        std::string guess;
        std::getline(std::cin, guess);
        //Now compare the guess to the target
        if(checkGuess(guess, targetNum) == 1)
        {
            std::cout << "Darn, you have bested me this time user. I Conceede." << std::endl;
            return 1;
        }
        
    }
    std::cout << "HA! I have bested and and proven that my intelgence is better than yours in this niche area of reasoning!" << std::endl;
    std::cout << "My number was " << targetNum << std::endl;
    std::cout << "Maybe try the easy setting next time. Not everyone needs to act like they are skynet out of the box." << std::endl;
    return 0;
}

int main()
{
    //set our random seed, we should only call this once, not everytime we generate a random number
    srand(time(NULL));
    int play = 1;
    while (play)
    {
        gameLoop();
        std::cout << "Would you like to play again? y/n" <<std::endl;
        std::string input;
        std::getline(std::cin, input);
        play = (input.find('y')!= std::string::npos) ? 1 : 0;
    }
    std::cout << "Thank you for playing. See you agin next time!" <<std::endl;
    
    return 0;
}
