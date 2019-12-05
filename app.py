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


multiple_choice_format("love", "hate")


    
def math_int():
    return

def true_or_false():
    return

def quiz_complete(*argv):
    return