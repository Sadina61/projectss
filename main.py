#data types
# string
#print("hello"[4])
#integer
#print(123 + 41)
#long integer
#print(123_384_189)
#float
#3.145
#boolean
#True
#False
# num=input("type a two digit number:")
# #print(type(num))
# first=num[0]
# second=num[1]
# print(int(first) + int(second))
#print(2 ** 3)
# print(3*(3+3)/3-3)

# weight=input("enter weight in kg:")
# height=input("enter height in m:")
# BMI=(int(weight)/ (float(height) ** 2))
# #bmi=int(BMI)
# print(round(BMI,3))
# print(8 // 3)
# age=input("enter your current age:")
# day= (90 * 365 - int(age) * 365 )
# month=(90 * 12 - int(age) *12 )
# week=(90 * 52 - int(age) * 52 )
# print(f"you have {day} days , you have {week}  weeks, you have {month} months")

# Project no 2

# print("Welcome to the Tip Calculator")
# bill=input("What was the total bill? $")
# tip=input("What percentage tip would you like to give ? 10, 12 or 15 ")
# people=input("How many people to split the bill ? ")
# Total= (float(bill)+ (int(tip)/100)*float(bill))/int(people)
# Final=round(Total,2)
# print(f"Each person should pay ${Final}")

# print("Welcome to the Rollercoaster")
# height=float(input( "What is yoir height in m? "))
# if height>4:
#   print("You can ride Rollarcoaster")
#   age=int(input("What is tour age?"))
#   if age<=18:
#     print("You have to pay $12")
#   else :
#     print("you have to pay $7")
# else :
#   print("You cannot ride a Rollarcoaster")

# num=int(input("Which number do you like to check?"))
# if num % 2 == 0:
#   print("Even Number")
# else:
#   print("Odd Number")

#leap year
# year=int(input("Enter the year"))
# if year%4==0:
#    if year%100==0 :
#      if year%400==0:
#       print("leap year")
#      else:
#       print("not a leap year")
  
#    else:
#     print("leap year")
# else:
#   print("not leap year")

# print("Welcome to Python Pizza Deliveries")
# size=input("What size of Pizza do you want? S, M or L ")
# add=input("Do you want Peperoni? Y or N ")
# extra=input("Do you want extra Cheese?Y or N ")
# s1=0
# s2=0
# if size=="S":
#   if add=="Y":
#     s1+=17
#   else:
#     s1+=15
# if size=="M":
#   if add=="Y":
#     s1+=23
#   else:
#     s1+=20
# if size=="L":
#   if add=="Y":
#     s1 +=28
#   else:
#     s1 +=25
# if extra=="Y":
#   s2= +1
# total_bill=(float(s1)+int(s2))
# print(f"Your final bill is  ${total_bill}")

#love calculator

# print("Welcome to the Love Calculator")
# name1=input("What is your name? ") 
# name2=input("What is your name? ")
# lower_case_name1=name1.lower()
# lower_case_name2=name2.lower()
# count1=int(lower_case_name1.count("t"))
# count2=int(lower_case_name1.count("r"))
# count3=int(lower_case_name1.count("u"))
# count4=int(lower_case_name1.count("e"))
# count5=int(lower_case_name1.count("l"))
# count6=int(lower_case_name1.count("o"))
# count7=int(lower_case_name1.count("v"))
# count8=int(lower_case_name1.count("e"))

# count11=int(lower_case_name1.count("t") )
# count22=int(lower_case_name1.count("r"))
# count33=int(lower_case_name1.count("u"))
# count44=int(lower_case_name1.count("e"))
# count55=int(lower_case_name1.count("l"))
# count66=int(lower_case_name1.count("o"))
# count77=int(lower_case_name1.count("v"))
# count88=int(lower_case_name1.count("e"))
# first=count1 + count2 + count3 + count4 + count11 + count22 + count33 + count44  
# second=count2 + count22 
# second=count5 + count6 + count7 + count8 + count55 + count66 + count77 + count88
# print(f"Your score is {first}{second}")

# print("Welcome to the Love Calculator")
# name1=input("What is your name? ") 
# name2=input("What is your name? ")
# lower_case_name1=name1.lower()
# lower_case_name2=name2.lower()
# joined= lower_case_name1+lower_case_name2
# T=int(joined.count("t") ) 
# R=int(joined.count("r"))
# U=int(joined.count("u"))
# E=int(joined.count("e"))
# first=T + R + U + E
# L=int(joined.count("l") ) 
# O=int(joined.count("o"))
# V=int(joined.count("v"))
# E=int(joined.count("e"))
# second=L + O + V + E
# score= str(first) + str(second)
# if int(score)<10 or int(score)>90:
#  print(f"Your score is {score}, you go together like coke and mentos!")
# if int(score)>40 and int(score)<50:
#    print(f"Your score is {score}, you are alright together!")
# else:
#   print(f"Your score is {score}")


#project no 3
# print('''
# __________
#   /\____;;___\
#  | /         /
#  `. ())oo() .
#   |\(%()*^^()^\
#  %| |-%-------|
# % \ | %  ))   |
# %  \|%________|

 
# ''')
# door_case = ""
# door = ""
# lake=""
# lake_case=""
# print("Welcome to the Treasure Island!!\n")
# print("Your mission is to find the treasure\n")
# road=input('You are at a cross road. Where do you  want to go? Type "left" or "right"\n')
# case_road=road.lower()
# if case_road=="left":
#   print("You are on trouble! There is a snake. GAME OVER!\n")
# else :
#   lake=input('You come to a lake.There is an island  in between the lake.Type "wait" to wait for a boat or type "swim" to swim across.\n')
#   lake_case=lake.lower()
#   if lake_case=="wait":
#     door=input('You arrive at the island unharmed.There is a house with 3 doors.One red, oneyellow , one blue.Which color do you chose?,R, Y , B ')
#     if door_case=="R":
#        print("GAME OVER!! There is fire inside  the door.")
#     elif door_case=="B":
#       print("GAME OVER!! There is poison inside the door.")
#     else :
#       print("HURRAY!, YOU WON THE TREASURES.")  
    
#   else :
#    print("GAME OVER!! There are crocodiles in the lake.")
#    door_case= door.upper()

# import random
# import my_module
# print(my_module.pi)

# random_integer=random.randint(1,10)
# print(random_integer)

# import random
# random_float=random.random()
# # print(random_float)
# actual=random_float*5
# print(actual)

# love_score=random.randint(1,100)
# print(f'Your love score is {love_score}')

# HEADS or TAILS
# import random
# side=random.randint(0,1)
# if side==0:
#   print("Head")
# else:
#   print("Tails")

# name_of_members=["Kumar","Bhawani","Sadina","Saphal"]
# name_of_members.append("Upreti")
# print(name_of_members)

#who will pay the bill??
# import random
# names_string=input("Give me everybody's names,separeted by comma. ")
# names= names_string.split(", ")
# total=len(names)
# random_choose=random.randint(0 , total - 1)
# person_who_will_pay=names[random_choose]
# person_who_will_pay=random.choice(names)
# print(person_who_will_pay  + "is going to buy the meal")

#treasure map
# row1 = ["🥸" , "🥸" , "🥸"]
# row2 = ["🥸" , "🥸" , "🥸"]
# row3 = ["🥸" , "🥸" , "🥸"]
# map=[row1 , row2 , row3]
# print(f"{row1}\n{row2}\n{row3}")
# position=input("Where do you want to put the treasure?")
# horizontal=(int(position[0]))
# vertical=(int(position[1]))
# selected_row=map[vertical-1]
# selected_row[horizontal-1]="X"
# print(f"{row1}\n{row2}\n{row3}")

#loop
# fruits=["Apple", "Pear", "Mango"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + "pie")

#average height
# student_height=input("Input a list of student heights. ").split()
# for n in range(0,len(student_height)):
#   student_height[n]=int(student_height[n])
# print(student_height)
# total_height=0
# for height in student_height:
#   total_height +=  int(height)
# print(total_height)
# number_of_student=0
# for student in student_height:
#   number_of_student += 1
# print(number_of_student)
# average_height=round(total_height / number_of_student)
# print(average_height)
 
#high score
# student_score = {}
# student_score=input("Input the list of student score.").split()
# for n in range(0,len(student_score)):
#  student_score[n] = int(student_score[n])
# print(student_score)
# max = 0
# for score in student_score:
#   if score > max:
#     max = score
# print(f"The highest score in the class is:  {max}")

# loop with range

# for number in range(1, 11, 2):
#  print(number)

#sum of even numbers
# sum=0
# for number in range (1,101,2):
#   sum += number
# print(sum)

#fizz buzzz
# for number in range (0,101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("Fizz")
#   elif number%3==0 and number%5==0:
#     print("Fizz Buzz")
#   else:
#    print(number)

import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '%', '$', '&', '(', ')', '+', '*']
print("Welcome to the PyPassword Generator")
no_letters=int(input("How many letters would you like in your password?\n" ))
no_numbers=int(input("How many numbers would you like in your password?\n" ))
no_symbols=int(input("How many symmbols would you like in your password?\n" ))
password_list=[]
for char in range(1,no_letters+1):
  password_list.append(random.choice(letters))

for char in range(1,no_numbers+1):
  password_list.append(random.choice(numbers))

for char in range(1,no_symbols+1):
  password_list.append(random.choice(symbols))
random.shuffle(password_list)
password=""
for char in password_list:
  password += char
print(f"Your password is {password}")


  


    





  

























  

 




  
       

 

  


  

