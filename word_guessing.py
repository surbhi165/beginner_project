import random

name  =  input("What is  your name?")
print("hello",name,"good luck for your game")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
guesses = []
failed  = 0
turns = 12

print("guessing the character......")

while True:
    guess =  input("guess a letter..")
    guesses.append(guess)
    failed  = 0
    for i in word:
        if i in guesses:
            print(i,end="")
        else:
            print("_")
            failed = failed+1
    print()

    if failed  == 0:
        print("you win")
        print("your word is...",word)
        break
    print()

    if guess not in word:
        turns  =  turns-1
        print("wrong")
        print("you have",+ turns ,"more guesses")

        if turns == 0:
            print("you loose")

