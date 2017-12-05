# Tony Yu
# 11/29/17
# Explore a weird cave!

import time
import random

print("<>"*44)
print("""
WELCOME TO
__   _   __  __ ___  __      _   _       ___     _  __       ___     ___    __  ___ 
 )_) /_) (_ ` )_) )  (_ `    / ` /_) \  / )_     /_) ) ) \  / )_  )\ ) ) / / )_) )_  
/ \ / / .__) /  _(_ .__)    (_. / /   \/ (__    / / /_/   \/ (__ (  ( ( (_/ / \ (__ """)
print("<>"*44)

time.sleep(1.2)
print()

print("You're taking a walk when you see a cave. You decide to go into it...")

time.sleep(1)
print()

tunnel_choice = input("You see the cave branch off into two tunnels.(type L for left, R for right): ").upper()

if tunnel_choice == "L":
    print("You walk into the left tunnel")
    time.sleep(1)
    lake_choice = input("You see a lake blocking your way. You also see a boat floating on it.(S for swim, B for boat, J for jump")
elif tunnel_choice == "R":
    print("You walk into the right tunnel")
else:
    print("Why didn't you choose a tunnel?")
    print("You just stand there for a few minutes until a cow comes and digests you") 


