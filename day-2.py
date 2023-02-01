print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10 or 12 "))
people = int(input("How many people to split the bill? "))
final_amount = round((bill/people)*(tip+100)/100,2)
final_amount = "{:.2f}".format((bill/people)*(tip+100)/100,2)
print(f"Each person should pay ${final_amount}.")


# two_digit_number = input("Type a two digit number: ")
# first = int (two_digit_number[0])
# second = int (two_digit_number[1])

# result = first + second

# print (result)

# 3+5
# 5-3
# 3*2
# 6/3
# 2**3

# PEMDAS
# **
# * / 
# + -
# round, //, %
# /=, +=, -=, *=

# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# # BMI = weight/(height)^2

# bmi = float(weight)/float(height)**2
# BMI = int(bmi) # int: 내림
# BMI_round = round(bmi,2) #반올림: 두번째 자리에서 반올림
# # //: 버림
# #print (BMI_round)
# # print (BMI)
# #print ("Your BMi is "+ str(BMI)) #str 귀찮아

# #f-string
# print (f"your bmi is {BMI}")