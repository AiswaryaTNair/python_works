import random
list=["notebook","school","table","candy","person","happy"]
word = random.choice(list)
length=len(word)
list1=["_"]*length
print(word)
hangman=9
#letter = input("enter the letter :")
while hangman!=0 and hangman<=9:
    letter = input("enter the letter :")
    if letter==word:
        print("succses")
        break
    if letter in word:
        guess=[]
        print(letter)
        guess.append(letter)
        print(guess)
        #length=len(word)
        #list1=["_"]*length
        print(list1)
        index=word.index(letter)
        list1[index]=letter
        print(index)
        print(list1) 
        
    else:
        hangman=hangman-1
        print(hangman)


if hangman==0:
    print("failed \n Game is over")  

"""
length=len(word)
list1=["_"]*length
print(list1)
index=word.index(letter)
list1[index]=letter
print(index)
print(list1)""" 



"""
length = len(word)
count = 0
display = '_' * length
already_guessed = []
play_game = ""
"""