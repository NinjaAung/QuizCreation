import os
from colorama import Fore, init
import random
import string


banner = '''                                                                                                                   
________        .__        __      _____          __  .__            
\_____  \  __ __|__| ____ |  | __ /     \ _____ _/  |_|  |__   ______
 /  / \  \|  |  \  |/ ___\|  |/ //  \ /  \\__  \\   __\  |  \ /  ___/
/   \_/.  \  |  /  \  \___|    </    Y    \/ __ \|  | |   Y  \\___ \ 
\_____\ \_/____/|__|\___  >__|_ \____|__  (____  /__| |___|  /____  >
       \__>             \/     \/       \/     \/          \/     \/ 
'''
os.system('clear')
print(50 * "_" + Fore.RED + banner + Fore.RESET + 50 * "_")


def multiple_choice_format(*argv):
    alphabet = list(string.ascii_lowercase)
    for (letter, option) in zip(alphabet, argv):
        print(f'{letter}. {option}')
    return input("Please enter a character a-e: ")

def question1():
    print("A rectangle has an area of 15 square centimeters.\nWhich of the following could be the rectangle's length and width?\n")
    if multiple_choice_format("1 and 15","2 and 15","15 and 15","7.4 and 3","6.99 and 4") == "b":
        print("\ngot em")
    else:
        print("\nno no")


question1()


def question2():
    print("")




    
def math_int():
    return

def true_or_false():
    return

def quiz_complete(*argv):
    return