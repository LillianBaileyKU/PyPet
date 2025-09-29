#This file is a part of PyPet
#Copyright (C) 2025 Lillian Bailey
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#PyPet is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with PyPet.  If not, see <https://www.gnu.org/licenses/>.






from tkinter import Tk, filedialog
import random
import time
import sys

# User defines petconfig filepath
Tk().withdraw()
filepath = filedialog.askopenfilename(title="Select your petconfig.txt file")
print("Copyright (C) 2025 Lillian Bailey")
print("This program comes with ABSOLUTELY NO WARRANTY; for details, refer to the LICENSE file")
print("This is free software, and you are welcome to redistribute it under certain conditions.")
option = int(input("Would you like to create a new pet (1 for new pet, 2 for existing pet)? "))

 # Initializing variables
with open(filepath, "r") as f:
    lines = f.readlines()

# Get values from txt document
def get_value(lines, linenum):
    line = lines[linenum]
    parts = line.split("=")
    return parts[1].strip()

if option == 1:
    name = input("Enter your pet's name: ")
    lines[0] = f"name = {name}\n"
    lines[1] = "food = 10\n"
    lines[2] = "clean = 10\n"
    lines[3] = "happy = 10\n"
    lines[4] = "health = 10\n"
    lines[5] = "dead = False\n"
    with open(filepath, "w") as f:
        f.writelines(lines)
    option = int(input("Would you like to see the tutorial (2 for no, 3 for yes)? "))

if option == 3:
    print("Welcome to your virtual pet!")
    print(f"You have given your virtual pet a name! Its name is {name}! From here on out, you will be charged with taking care of it!")
    time.sleep(2)
    print("Every time you open your pet's home, it will have gotten up to something! You will be given a brief rundown of its activities and then tasked with the following: ")
    print("Feeding your pet: Type feed into the command bar to feed your pet!")
    print("Cleaning your pet: Type clean into the command bar to clean your pet!")
    print("Entertaining your pet: Type play into the command bar to play with your pet!")
    print("Keep your pet's stats high or they'll lose health! We wouldn't want them to die!")
    print("Enter exit into the command bar to end the program and save your information!")
    time.sleep(8)
    print("DO NOT EDIT PETCONFIG.TXT OR IT WILL BREAK THE SCRIPT. IF BROKEN, PASTE AS DEFINED ON GITHUB TO RESET. ALL VARIABLES SHOULD BE ON THEIR OWN LINES!")
    print("Good luck! Enjoy your pet!")
    time.sleep(2)
    option = 2

if option == 2:
    name = get_value(lines, 0)
    food = int(get_value(lines, 1))
    clean = int(get_value(lines, 2))
    happy = int(get_value(lines, 3))
    health = int(get_value(lines, 4))
    dead = get_value(lines, 5) == "True"

    minusfood = random.randint(1, 3)
    minusclean = random.randint(1, 3)
    minushappy = random.randint(1, 3)

    food = food - minusfood
    clean = clean - minusclean
    happy = happy - minushappy
    if food < 3 or clean < 3 or happy < 3:
        health -= 3
    elif food <= 5 and food > 3 or clean <= 5 and clean > 3 or happy <= 5 and happy > 3:
        health -= 2
    if health <= 0:
        dead = True
        
    if dead != True:
        print(f"Welcome to your home, with your pet {name}!")
        print(f"Your pet lost {minusfood} hunger points!")
        print(f"Your pet rolled around in {minusclean} mud puddles!")
        print(f"Your pet is {minushappy} times less happy today!")

        print("=============================")
        print(f"Pet Name: {name}")
        print(f"Food: {food}")
        print(f"Cleanliness: {clean}")
        print(f"Happiness: {happy}")
        print(f"Health: {health}")

while True:
    if health <= 0:
        dead = True
        break
    choice = input("Enter your action: ")
    if choice == "feed":
        food = 10
        print(f"{name} has been fed!")
        print("=============================")
        print(f"Pet Name: {name}")
        print(f"Food: {food}")
        print(f"Cleanliness: {clean}")
        print(f"Happiness: {happy}")
        print(f"Health: {health}")
        choice = "n"
    elif choice == "clean":
        clean = 10
        print(f"You've given {name} a bath!")
        print("=============================")
        print(f"Pet Name: {name}")
        print(f"Food: {food}")
        print(f"Cleanliness: {clean}")
        print(f"Happiness: {happy}")
        print(f"Health: {health}")       
        choice = "n"
    elif choice == "play":
        happy = 10
        print(f"You played with {name}!")
        print("=============================")
        print(f"Pet Name: {name}")
        print(f"Food: {food}")
        print(f"Cleanliness: {clean}")
        print(f"Happiness: {happy}")
        print(f"Health: {health}")
        choice = "n"
    elif choice == "exit":
        if food == 10 and clean == 10 and happy == 10 and health + 2 <= 10:
            health += 2
        elif food == 10 and clean == 10 and happy == 10 and health + 2 > 10 and health + 1 <= 10:
            health += 1
        print(f"Exiting your pet's home! {name} is excited to see you soon!")
        lines[1] = f"food = {food}\n"
        lines[2] = f"clean = {clean}\n"
        lines[3] = f"happy = {happy}\n"
        lines[4] = f"health = {health}\n"
        lines[5] = f"dead = {dead}\n"
        with open(filepath, "w") as f:
            f.writelines(lines)
        time.sleep(2)
        sys.exit()

if dead == True:
    print(f"I'm sorry, but your pet {name} has died. They were not given the proper treatment, and their health diminished to 0. Please make a new pet to continue.")
    time.sleep(5)
    sys.exit()