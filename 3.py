print('''
__________
  /\____;;___\
 | /         /
 `. ())oo() .
  |\(%()*^^()^\
 %| |-%-------|
% \ | %  ))   |
%  \|%________|


''')
door_case = ""
door = ""
lake=""
lake_case=""
print("Welcome to the Treasure Island!!\n")
print("Your mission is to find the treasure\n")
road=input('You are at a cross road. Where do you  want to go? Type "left" or "right"\n')
case_road=road.lower()
if case_road=="left":
  print("You are on trouble! There is a snake. GAME OVER!\n")
else :
  lake=input('You come to a lake.There is an island  in between the lake.Type "wait" to wait for a boat or type "swim" to swim across.\n')
  lake_case=lake.lower()
  if lake_case=="wait":
    door=input('You arrive at the island unharmed.There is a house with 3 doors.One red, oneyellow , one blue.Which color do you chose?,R, Y , B ')
    if door_case=="R":
       print("GAME OVER!! There is fire inside  the door.")
    elif door_case=="B":
      print("GAME OVER!! There is poison inside the door.")
    else :
      print("HURRAY!, YOU WON THE TREASURES.")  

  else :
   print("GAME OVER!! There are crocodiles in the lake.")
   door_case= door.upper()