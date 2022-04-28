# Wordle_Solver
The code will solve wordle when given a word to solve. 

Main.py: The code that allows you to play wordle in a simple way using input and printing

solver1.py: This code just eliminates words if they are not possible. Then, just a random word from the remaining words. 

solver2.py: This uses the solver1.py word eliminating algoritm, but uses a preprocessing method which sorts the words by whether they don't have repeating letters in the word. It will sort the words remaining for the first two guesses then it will just select whatever is the first word in the list.
