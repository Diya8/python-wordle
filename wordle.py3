import words, random
import pyperclip
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

keyboard_keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                  ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
                  ["Z", "X", "C", "V", "B", "N", "M"]]

keyboard_colors = {"A"	:	"BLUE"	,
"B"	:	"BLUE"	,
"C"	:	"BLUE"	,
"D"	:	"BLUE"	,
"E"	:	"BLUE"	,
"F"	:	"BLUE"	,
"G"	:	"BLUE"	,
"H"	:	"BLUE"	,
"I"	:	"BLUE"	,
"J"	:	"BLUE"	,
"K"	:	"BLUE"	,
"L"	:	"BLUE"	,
"M"	:	"BLUE"	,
"N"	:	"BLUE"	,
"O"	:	"BLUE"	,
"P"	:	"BLUE"	,
"Q"	:	"BLUE"	,
"R"	:	"BLUE"	,
"S"	:	"BLUE"	,
"T"	:	"BLUE"	,
"U"	:	"BLUE"	,
"V"	:	"BLUE"	,
"W"	:	"BLUE"	,
"X"	:	"BLUE"	,
"Y"	:	"BLUE"	,
"Z"	:	"BLUE"	}

def print_keyboard():
    print()
    for line in range(3):
        for letter in keyboard_keys[line]:
            COLOR = "bcolors."+keyboard_colors[letter]
            print(f"{eval(COLOR)}{letter}{bcolors.ENDC}", end=" ")
        print()
        print(" "*(line+1), end="")
    print()


def pick_word():
    return random.choice(words.words_list)

def is_word(guess):
    return guess in words.words_list

def letter_checker(guess, picked_word, output_list, grid_list):
    print()
    grid_list += "\n"
    for output in output_list:
        print(output)
    guess = guess.upper()
    pickle = picked_word.upper()
    output = ""
    for letter in range(5):
        if guess[letter] == pickle[letter]:
            keyboard_colors[guess[letter]] = "GREEN"
            COLOR = "bcolors."+keyboard_colors[guess[letter]]
            print(f"{eval(COLOR)}{guess[letter]}{bcolors.ENDC}", end="")
            output += f"{eval(COLOR)}{guess[letter]}{bcolors.ENDC}"
            grid_list += "\U0001F7E9"
        elif guess[letter] in pickle:
            turn_back = False
            if keyboard_colors[guess[letter]] == "GREEN":
                turn_back = True
            keyboard_colors[guess[letter]] = "YELLOW"
            COLOR = "bcolors."+keyboard_colors[guess[letter]]
            print(f"{eval(COLOR)}{guess[letter]}{bcolors.ENDC}", end="")
            output += f"{eval(COLOR)}{guess[letter]}{bcolors.ENDC}"
            if turn_back:
                keyboard_colors[guess[letter]] = "GREEN"
            grid_list += "\U0001F7E8"
        else:
            keyboard_colors[guess[letter]] = "RED"
            COLOR = "bcolors."+keyboard_colors[guess[letter]]
            print(f"{eval(COLOR)}{guess[letter]}{bcolors.ENDC}", end="")
            output += f"{eval(COLOR)}{guess[letter]}{bcolors.ENDC}"
            grid_list += "\U00002B1B"
    print()
    output_list.append(output)
    return grid_list

picked_word = pick_word()
guess_number = 1
win = False
grid_list = ""
output_list = []
while guess_number < 7:
    print_keyboard()
    guess = input("Enter your guess: ").lower()
    if guess == picked_word:
        print(f"\nYou have won!\U0001F973 {guess_number}/6\n")
        win = True
        grid_list += "\n\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9"
        break
    elif is_word(guess) and len(guess) == 5:
        grid_list = letter_checker(guess, picked_word, output_list, grid_list)
    else:
        print("\nInvalid word! Try again.\n")
        continue
    guess_number += 1
if not win:
    print(f"\nThe word was {bcolors.BOLD}{picked_word.upper()}{bcolors.ENDC}. Better luck next time!\n")
    guess_number = "X"
print("Share \U0001F917")
print(f"Wordle {guess_number}/6 \n{grid_list}\n\nCopied to clipboard!\n")

pyperclip.copy(f"Wordle {guess_number}/6 \n{grid_list}")