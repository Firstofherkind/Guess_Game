# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 13:20:38 2021

@author: JENI
"""

import random


print('Welcome to a Game of Random Numbers!!')
print("Rule of this Game is to make random guesses between Numbers, which in this case is between 1 and 10.")
print('Have fun playing!! xoxo!!')
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Enter a number between 1 and {x}: \n'  ))
        if guess > random_number:
            print('Number too high, Guess again.')
        elif guess < random_number:
            print('Number too low, guess again.')
        else:
            print('Yayyyyy!!! You guessed correctly!')



guess(10)
