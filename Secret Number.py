# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 13:48:01 2021

@author: deyasini
"""

high=100
low=0
print("Please think of a number between 0 and 100!")
ans=round((low+high)/2)
print("Is your secret number "+str(ans))
user=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while user!='h' and user!='l' and user!='c':
    print("Sorry, I did not understand your input.")
    print("Is your secret number"+str(ans))
    user=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while user!='c':
    if user=='l':
     low=ans
    if user=='h':
     high=ans
    ans=round((low+high)/2)
    print("Is your secret number "+str(ans))
    user=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    while user!='h' and user!='l' and user!='c':
        print("Sorry, I did not understand your input.")
        print("Is your secret number"+str(ans))
        user=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
print("Game over. Your secret number was: "+str(ans))