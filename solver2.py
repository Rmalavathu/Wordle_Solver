#To do this solver we will use preproccessing to sort the list in the beginning so words with lots of letters are guessed first than words with repeats. After this I can try to sort words by patterns

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

all_words = []
words = []
myfile = open(r'C:\Users\4mroh\PycharmProjects\wordleAI\words.txt')
lines = myfile.readlines()
for word in lines:
    words.append(word[:5])
all_words = words
word_solve = "depot"
print(word_solve)

def preprocess():
    global words
    global letters
    good = []
    bad = []
    for x in words:
        total = 0
        for y in letters:
            if y in x:
                total += 1
        if total != 5:
            bad.append(x)
        else:
            good.append(x)
    return (good + bad)

def deleteWords(letter, pos, color):
    global words
    removal = []
    for x in words:
        if (letter in x) and color == "B":
            removal.append(x)
        elif color == "G":
            if letter != x[pos]:
                removal.append(x)
        elif color == "Y":
            if letter == x[pos]:
                removal.append(x)
    ans = [i for i in words if i not in removal]
    return ans

def wordleCheck(ans, check):  # ans is the answer word to check with, check is word that is being checked
    chars = list(ans)
    result = ""
    i = 0
    for letter in check:
        if ans[i] == letter:
            result += "G"
        elif letter in chars:
            result += "Y"
        else:
            result += "B"
        i += 1
    return result

def turn(guess, result):
    global words
    loc = 0
    while loc < 5:
        words = deleteWords(guess[loc], loc, result[loc])
        loc += 1

words = preprocess()
guess = []
turns = 0

while turns < 10:
    if turns < 2:
        words = preprocess()
    if turns == 0:
        current_guess = "slate"
    else:
        current_guess = words[0]
    result = wordleCheck(word_solve, current_guess)
    print(f'Guess {turns + 1}: {current_guess} \nresult: {result}')
    turn(current_guess, result)
    turns += 1
    if (result == 'GGGGG'):
        print(f"DONE IN {turns} TURNS")
        quit()






