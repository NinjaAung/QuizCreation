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


def multiple_choice_format(answer, *argv):
    alphabet = list(string.ascii_lowercase)
    for (letter, option) in zip(alphabet, argv):
        print(f'{letter}. {option}')
    print()
    if input("Please enter a character a-e: ") == answer.lower or answer:
        return 1
    else:
        return 0

def question_format(number, question, answer):
    os.system('clear')
    print(f'\n{number}. {question}\n')
    if not answer.isdigit():
        if input("Please enter a character T or F: ") == answer.lower() or answer:
            return 1
        else:
            return 0
    else:
        if input("Please Enter a numeral: ") == answer:
            return 1
        else:
            return 0


def question1_multiple():
    os.system('clear')
    print("\n1. A rectangle has an area of 15 square centimeters.\nWhich of the following could be the rectangle's length and width?\n")
    return multiple_choice_format("b", "1 and 15", "2 and 15", "15 and 15", "7.4 and 3", "6.99 and 4")

def question2_multiple():
    os.system('clear')
    print("\n2. Which of the following are factor pairs for 49?\n")
    return multiple_choice_format("b", "3 and 13", "1 and 49", "7 and 8", "4 and 11", "2 and 23") 

def question3_tf():
    return question_format("3", "Is 7 a odd number?", "T")
    
def question4_tf():
    return question_format("4", "Is ((2^2)^3) = 2^5", "F")

def question5_int():
    return question_format("5", "There are 49 dogs signed up to compete in the dog show.\nThere are 36 more small dogs than large dogs signed up to compete.\nHow many small dogs are signed up to compete?", "42")
def question6_int():
    return question_format("6", "A man buys a horse for $60.\n He sells the horse for $70. He then buys the horse back for $80.\n And he sells the horse again for $90. In the end, how much money did the man make or lose? Or did he break even?", "20")



def quiz_complete(*argv):
    if sum(argv) >= 5:
        print("\n\nwow you are a the supreme math wiz. You got " + str(sum(argv)) + " correct!")
    elif sum(argv) >= 3:
        print("\n\nBetter luck next time. You got " + str(sum(argv)) + " correct!")
    elif sum(argv) >= 2:
        print("\n\nDon't worry you got this, keep practising. You got " + str(sum(argv)) + " correct!")

quiz_complete(question1_multiple(), question2_multiple(), question3_tf(), question4_tf(), question5_int(), question6_int())