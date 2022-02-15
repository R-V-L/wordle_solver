# Wordle Solver

This is my take on a solver for the internet game [Wordle](https://en.wikipedia.org/wiki/Wordle)  
Whenever it's finished it should be able to solve it for you, giving you a list of posible words on each step and (hopefully) being able to solve it before you run out of attempts.  

It should work like this:  
1.- Gets a file containing all the words in whatever language you choose and downloads it
2.- Creates a list with all the 5 digits long words (configurable) in the previously downloaded file. You should have an option to normalize each word before addding it to the list
3.- For your first attempt, you will get a random word.
4.- Filter out results based on the following criteria:
    - Contains X letter
    - Doesn't contain X letter
    - Letter in n position equals x
    - Letter in x position is different to x

If you are reading this either: this project is not complete but i'm working on it, this project is not complete and i'm working on something else or this project IS complete but i forgot to remove this.