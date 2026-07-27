hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random
word=["bad", "good", "ugly"]
rand_word=random.choice(word)
display=[" _"] * len(rand_word)
print(" ".join(display))
gessed=[]
num=6
print(hangman[0])
while "".join(display)!=rand_word and num>0:
    gess=input("please enter a letter:").lower()
    if gess in gessed:
        print("you already enter then.try again:")
        continue
    else:
        gessed.append(gess)
    if gess not in rand_word:
        num-=1
        print(hangman[6-num])
    for x in range(len(rand_word)):
        if rand_word[x]==gess:
            display[x]=gess
    print(" ".join(display))
    print(f"you have {num} more than.")
if num==0:
    print("""
    *********
    You Lose!
    *********""")
else:
    print("""
    *********
    You Win!
    *********""")
