"""
Hangman.

Authors: Samuel VanDenburgh and Valeria Paiz.
"""  #Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! ######
import random

def pick_word():
    lenght = int(input('Please type in the minimum length for your word'))
    with open('words.txt') as f:
        f.readline()
        string = f.read()
    words = string.split()
    r = random.randrange(0, len(words))
    picked = words[r]
    while len(picked) < lenght:
        r = random.randrange(0, len(words))
        picked = words[r]
    print(picked)
    return picked

def set_difficulty():
    wrong = int(input('How many wrong attempts would you like to allow'))
    print('you have allowed', wrong, 'wrong attempts')
    return wrong

def display_lines(word):
    list = []
    for k in range (len(word)):
        list.append('-')
        print(list[k],end='')
    print()
    return list

def ask_letter():
    letter = input('Guess a Letter')
    return letter

def check_letter(letter, word, lines, wrong):
    initial = []
    for k in range(len(lines)):
        initial.append(lines[k])
    for k in range(len(word)):
        if letter == word[k]:
            lines[k] = letter
        print(lines[k], end='')
    print()
    if lines == initial:
        print(letter, 'is not in the word')
        wrong = wrong_attempt(wrong)
        return wrong
    else:
        return lines


def wrong_attempt(wrong):
    wrong = wrong + 1
    return wrong



def main():
    wrong = 0
    word = pick_word()
    mistakes_allowed = set_difficulty()
    lines = display_lines(word)
    while True:
        letter = ask_letter()
        check = check_letter(letter, word, lines, wrong)
        if check == word:
            print('You Won')
        if type(check) is int:
            wrong = check
            if check >= mistakes_allowed:
                print('Game Over')
                break


main()