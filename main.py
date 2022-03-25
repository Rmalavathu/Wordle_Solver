# RUNNING WORDLE WITH USER INPUT
# This is a simple way to play wordle
# Might consider including GUI to have good user input
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


answer = "later"  # the answer for wordle

i = 1
while i != 6:
    guess = input("Guess ").lower()
    output = wordleCheck(answer, guess)
    print("     ", output)
    if output == "GGGGG":
        i = 6
    else:
        i += 1
