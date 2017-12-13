# Tony Yu
# 11/29/17
# Explore a weird cave!
 
def left_tunnel():
    print("You walk into the left tunnel")
    time.sleep(1)
    print("You see a lake blocking your way. You also see a boat floating on it.")
    lake_choice = input("Enter S for swim, B for boat, J for jump: ").upper()
    return lake_choice

def right_tunnel():
    print("You walk into the right tunnel")
    time.sleep(1)
    print("You see a rope leading into a hole and also see light from a torch in the distance")
    rope_choice = input("Enter R to climb down the rope or T to go to the torch: ").upper()
    return rope_choice

def torch_death():
    print("You walk into a cave with the torch in it")
    time.sleep(1)
    print("Suddenly, a trapdoor opens beneath you and you fall down a die")

def dragon_choice():
    choice = input("What do you do?(K for kill or R for run): ").upper()

key = "open sesame"

import time
import random

print("<>"*44)
print("""
WELCOME TO
  ____ _____ _      _  __     _______    _____     __      ________            _______      ________ _   _ _______ _    _ _____  ______ 
 |  _ \_   _| |    | | \ \   / / ____|  / ____|   /\ \    / /  ____|     /\   |  __ \ \    / /  ____| \ | |__   __| |  | |  __ \|  ____|
 | |_) || | | |    | |  \ \_/ / (___   | |       /  \ \  / /| |__       /  \  | |  | \ \  / /| |__  |  \| |  | |  | |  | | |__) | |__   
 |  _ < | | | |    | |   \   / \___ \  | |      / /\ \ \/ / |  __|     / /\ \ | |  | |\ \/ / |  __| | . ` |  | |  | |  | |  _  /|  __|  
 | |_) || |_| |____| |____| |  ____) | | |____ / ____ \  /  | |____   / ____ \| |__| | \  /  | |____| |\  |  | |  | |__| | | \ \| |____ 
 |____/_____|______|______|_| |_____/   \_____/_/    \_\/   |______| /_/    \_\_____/   \/   |______|_| \_|  |_|   \____/|_|  \_\______|""")
print("<>"*44)

time.sleep(1.2)
print()

print("You're taking a walk when you see a cave. You decide to go into it...")

time.sleep(1)
print()

tunnel_choice = input("You see the cave branch off into two tunnels.(type L for left, R for right): ").upper()

if tunnel_choice == "L":
    lake_choice = left_tunnel()
    if lake_choice == "S" or lake_choice == "SWIM":
        print("You jump in the freezing water and start swimming")
        print("You realize you never learned how to swim...")
        time.sleep(1.2)
        print("But you start doggy paddling and realize you can swim this way")
        # Remember to add winning text
    elif lake_choice == "B" or lake_choice == "BOAT":
        print("You climb into the boat and realize you have no paddle")
        print("The boat starts drifting away from the edge...")
        time.sleep(1.4)
        boat_choice = input("What do you do?(E for escape the boat or S for stay): ").upper()
        if boat_choice == "E": 
            print("You try to jump ashore but fail and drown")
        elif boat_choice == "S":
            print("You stay there, and a giant rubber duck starts drifting towards you and crushes you")
        elif boat_choice == ("OPEN SESAME"):
            print("""Once upon a time, there was a player. He wanted to find all the secrets of the game.
He decided he wanted to say open seasame! He saw this text, and died. THE END """)
            time.sleep(5)
            print("YOU DIED")
        else:
            print("NOPE")
    elif lake_choice == "J" or lake_choice == "JUMP":
        print("You try to jump over the lake but fall in and drown")
    else:
        print("THAT IS NOT VALID OPTION")
        print("SELF DESTRUCTING COMPOTER",end='')
        time.sleep(0.8)
        print(".",end='')
        time.sleep(0.8)
        print(".",end='')
        time.sleep(0.8)
        print(".",end='')
        print("YOUR COMPOTER JUST EXPLODED")
        
elif tunnel_choice == "R" or cave_choice == "RIGHT":
    rope_choice = right_tunnel()
        
    if rope_choice == "R":
        print("You start climbing down the rope...")
        time.sleep(1.4)
        print("But you slip and fall!")
        time.sleep(1.4)
        print("But thankfully land softly")
        time.sleep(1)
        print("You look around and see a gigantic grey dragon slumbering!!!")
        choice = dragon_choice()
        if choice == "K" or choice == "KILL":
            print("You try to kill it using a rock, and realize its already dead!")
            time.sleep(1)
            print("You walk over it and see a chest full of treasure!!!")
            time.sleep(1)
            print("You manage to pick it up and carry it to your house. YOU WIN!!!")
            
        elif choice == "R" or choice == "RUN":
            print("You run away put trip on a rock and die")
            
        else:
            print("The dragon wakes up and swallows you")
    elif rope_choice == "T":
        print("You start walking to the torch...")
        time.sleep(1)
        print("You start to pick up the torch when a rock falls down from the ceiling and crushes you")

    else:
        print("You stand there until a thin and bony finger pushes you down the hole and you die")
        
    
else:
    print("Why didn't you choose a tunnel?")
    print("You just stand there for a few minutes until a cow comes and digests you") 


