# -*- coding: utf-8 -*-
###Write a Python program that runs repeatedly and prompts the user to enter a number – it should stop when the user enters a sentinel value. Once all numbers are entered, the program should print the following information using one of the methods provided by Python:
###1. The number of numbers entered in the list
###2. The smallest value in the list
###3. The largest value in the list
###The program should use iteration, a list, and user-defined functions.



######
######



def guessTracker():
    answers = []
    key = 100
    flag = True
    while flag:
        input = raw_input('Guess a number:')
        try:
            x = float(input)
            answers = answers + [x]
            if x == key:
                print 'You guessed correctly! Good job, Champ.'
                print ('Your guesses were', answers)
                print ('Your highest guess was', max(answers))
                print ('Your lowest guess was', min(answers))
                flag = False
            elif x < key:
                print 'too low try again'     
            elif x > key:
                print 'too big try again'
        except:
            print('this program does not recognize ', str(input), ' as a number')
#guessTracker()           













def print_List_High_Low(mylist):
    print ('Your guesses were ' + str( mylist) + '.')
    print ('Your highest guess was ' + str(max(mylist)) + '.')
    print ('Your lowest guess was ' + str(min(mylist)) + '.')
           

def guessTracker2():
    answers = []
    key = 100
    flag = True
    while flag:
        input = raw_input('Guess a number:')
        try:
            x = float(input)
            answers = answers + [x]
            if x == key:
                if len(answers) == 1:
                    print('Damn you are good!')
                    print_List_High_Low(answers)
                    flag = False
                else:
                    print 'You guessed correctly! Good job, Champ.'
                    print_List_High_Low(answers)
                    flag = False
            elif x < key:
                print 'Too low try again.'     
            elif x > key:
                print 'Too big try again.'
        except:
            print('this program does not recognize ', str(input), ' as a number.')
#guessTracker2()










import random

def guessTracker3():
    answers = []
    key = random.randrange(1,100)
    flag = True
    while flag:
        input = raw_input('Guess an integer between 1 and 99:')
        try:
            x = float(input)
            answers = answers + [x]
            if x == key:
                if len(answers) == 1:
                    print 'You guessed correctly! Good job, Champ.'
                    print('Damn you are good!')
                    flag = False
                else:
                    print 'You guessed correctly! Good job, Champ.'
                    print_List_High_Low(answers)
                    flag = False
            elif x < key:
                print 'Too low try again.'     
            elif x > key:
                print 'Too Big try again.'
        except:
            print('This program does not recognize ', str(input), ' as a number.')
            
#guessTracker3()




import math

def guessTracker4():
    
    ### Asks user to create range
    maxnumber = 0
    while maxnumber == 0:
        PotentialMax = raw_input('Enter upper bound for range of numbers to pick from, an integer greater than 1:')
        
        ###Type check user input 
        try:   
            if int(float(PotentialMax)) == float(PotentialMax):
                if float(PotentialMax) > 1:
                    maxnumber = int(float(PotentialMax))
                else:
                    print (PotentialMax, ' is not an integer greater than 1.')
            else:
                print (PotentialMax, ' is not an integer greater than 1.')
        except:
            print (PotentialMax, ' is not an integer greater than 1.') 
            
                    
    ###Computes the max number of guesses it would take to guess using binary search.
    if int(math.log(maxnumber,2)) == math.log(maxnumber,2):
        binary_guess_max = int (math.ceil(math.log(maxnumber,2)))+1
    else:
        binary_guess_max = int (math.ceil(math.log(maxnumber,2)))
    print ('You should be able to guess correctly in ' + str(binary_guess_max) + ' guesses or less.')
    
    ### create answerlist, random key
    answers = []
    key = random.randrange(1, maxnumber + 1)
    
    ### Ask for user input repeatedly, flag will be set to false when correct number is guessed.
    flag = True
    while flag:
        input = raw_input('Guess an integer between 1 and ' + str(maxnumber) + ': ')
        
        ###check input for type and value, return different messages based on number of guesses.
        try:
            x = float(input)
            answers = answers + [x]
            if x == key:
                if len(answers) == 1:
                    print 'You guessed correctly! Damn you are good!'
                    print_List_High_Low(answers)
                    flag = False
                elif len(answers) <= binary_guess_max:
                    print ('You guessed correctly! It took you ' + str(len(answers)) + ' guesses. Good job, Champ.' )
                    print_List_High_Low(answers)
                    flag = False
                else:
                    print ('You guessed correctly, but it took more than ' + str(binary_guess_max) + ' guesses... meh.')
                    print_List_High_Low(answers)
                    flag = False
                    
            ###Give user a hint for next guess if guess is incorrect
            elif x < key:
                print 'Too low try again.'     
            elif x > key:
                print 'Too big try again.'
                
        ###Exception statement if user input is invalid.
        except:
            print('This program does not recognize' + str(input) + ' as a number.')
            
guessTracker4()