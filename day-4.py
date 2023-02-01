#1.Assign
import random

random_integer = random.randint(1,10)
print(random_integer)

#0.00000 - 0.99999
random_float = random.random()
print(random_float)
#random_float * 5 => 0-4.999 사이 랜덤 넘버

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

#2.Assign
import random

random_side = random.randint(0,1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

#3.Assign
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#프린트
print(states_of_america[-2])

#데이터변경 후, 출력하기
states_of_america[1] = "Pencil"
print(states_of_america[1])

#데이터 추가
states_of_america.append("Heesun") 
print(states_of_america)

#데이터 추가
states_of_america.extend(["Heesun","Yi-wei"]) 
print(states_of_america)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]