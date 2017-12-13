# Tony Yu
# 12/12/17
# Def practice

import math

##def cheese():
##    print("I LIKE CHEESE "*100)
##
##cheese()

##def temp_c(temp_f):
##    '''Converts a temperature in Fahrenheit to Celsius'''
##    answer = (temp_f - 32) * (5/9)
##    return answer
##
##while "0" == "0":
##    t_in_f = input("Please enter a temperature in Fahrenheit: ")
##    t_in_f = float(t_in_f)
##    t_in_c = temp_c(t_in_f)
##
##    print("That temperature in Celsius is",t_in_c) 

##def vol_sphere(radius):
##    '''Calculates the volume of a sphere'''
##    volume = (4/3)*math.pi*r**3
##    return volume
##
##r = input("Please enter the radius of the sphere you want to know the volume of: ")
##r = float(r)
##v_sphere = vol_sphere(r)
##if v_sphere > 100:
##    print("Thats a huge sphere!")
##else:
##    print("Thats a small sphere!")
##
##print("The volume of the sphere is", v_sphere)

def hamburger(wish):
    if wish.lower() in ["no","nope","they are the worst"]:
        reply = "WHY DO YOU NOT LIKE HAMBURGERS"
    elif wish.lower() in ["yes","yup","yip"]:
        reply = "Yay! Hamburgers are the best"
    else:
        reply = "What?"
    return reply
        
wish = input("Do you like hamburgers: ")
print(hamburger(wish))

