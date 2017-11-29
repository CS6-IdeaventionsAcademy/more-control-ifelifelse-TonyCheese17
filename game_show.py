# Tony Yu
# 11/28/17
# GET A NEW CAR NOW

import random
import time

count = 0
count2 = 0

letter = "$"
letter2 = "$"

while count <= 34:
    print(letter,end='')
    time.sleep(0.06)
    count = count + 1

print()

print("WELCOME TO THE FATSIE GAME SHOW!!!")

while count2 <= 34:
    print(letter2,end='')
    time.sleep(0.06)
    count2 = count2 + 1

print()
print()

time.sleep(0.8)

name = input("Please enter your name first: ")

print()


time.sleep(0.6)

print("Hi there " + name + """! So, this is how the game show works.
You will have to choose from 4 doors. Each door has a different prize! Good luck!""")

print()

time.sleep(2)

door1 = ("You won a banana! Good job.")

door2 = ("You won a brand new 8K quantum dot TV! Good job.") 

door3 = ("You got a brand new broken PS4! Good job.")

door4 = ("You got a new pet rock! Good job.")

guess = input("Guess a door!(1,2,3 or 4): ")

if guess == "1":
    print(random.choice([door1, door2, door3, door4]))
elif guess == "2":
    print(random.choice([door1, door2, door3, door4]))
elif guess == "3":
    print(random.choice([door1, door2, door3, door4]))
elif guess == "4":
    print(random.choice([door1, door2, door3, door4]))
elif guess:
    print("Why didn't you choose a door??? Don't you want a prize?")
