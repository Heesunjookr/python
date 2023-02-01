
#1.Assign
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
 print("This is a even number.")
else:
 print("This is an odd number.")


#2.Assign
print("Welcome to the rollercoaster!")
Height = int(input("What is your height?"))

if Height >= 120:
    print ("You can ride the rollercoaster!")
    age = int(input("How old are your?"))
    if age <= 18:
        print("You should pay $7.")
    else:
        print("You should pay $10.")
else:
    print("You have to grow taller to ride the rollercoaster.")

#3.Assign
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight/height**2)
#round: 반올림

if BMI <= 18.5:
  print(f"Your BMI is {BMI} and underweight.")
elif 18.5 < BMI <= 25:
  print(f"Your BMI is {BMI} and a normal weight.")
elif 25 < BMI <= 30:
  print(f"Your BMI is {BMI} and overweight.")
elif 30 < BMI <= 35:
  print(f"Your BMI is {BMI} and ovese.")
else:
  print(f"Your BMI is {BMI} and clinically obese.")

#4.Assign
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  print(f"{year} is leap year.")
elif year % 100 == 0:
    print (f"{year} is not Leap year.")
elif year % 400 == 0:
  print(f"{year} is leap year.")
else:
  print(f"This {year} is not leap year.")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("leap year")
        else :
            print ("not leap year")
    else :
        print ("leap year")
else :
    print ("not leap year")

#5.Assign
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

#6.Assign
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0 

if size == "S":
  bill += 15
elif size == "M":
  bill += 20 
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is ${bill}")

#7.Assign
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1+name2
lower_string = combined_string.lower()
t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

true = t+r+u+e

#Final
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")