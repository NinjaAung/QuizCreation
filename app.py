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
    print()
    return input("Please enter a character a-e: ")

def true_or_false(number, question, answer):
    print(f'\n{number}. {question}\n')
    if answer.isdigit():
        if input("Please enter a character T or F: ") == answer:
            return 1
        else:
            return 0
    else:
        if input("Please Enter a numeral: ") == answer:
            return 1
        else:
            return 0


def question1_multiple():
    print("\n1. A rectangle has an area of 15 square centimeters.\nWhich of the following could be the rectangle's length and width?\n")
    if multiple_choice_format("1 and 15","2 and 15","15 and 15","7.4 and 3","6.99 and 4") == "b":
        return 1
    else:
        return 0

def question2_multiple():
    print("\n2. Which of the following are factor pairs for 49?\n")
    if multiple_choice_format("3 and 13", "1 and 49", "7 and 8", "4 and 11", "2 and 23") == "b":
        return 1
    else:
        return 0  

def question3_tf():
    true_or_false("3", "Is 7 a odd number?", "T")
    
def question4_tf():
    return

def question5_int():
    return
def question6_int():
    return



def quiz_complete(*argv):
    print(argv)

quiz_complete(question1_multiple(), question2_multiple())