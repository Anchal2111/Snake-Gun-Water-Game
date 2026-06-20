
# snake gun and water game 

import random

computer = random.choice([1,0,-1])
user_choice = input("enter your choice: ")

dict = {
    "s" : 1,
    "g" : 0,
    "w" : -1
}

reverse_Dict = {
    1 : "Snake",
    0 : "Gun",
    -1 : "Water"
}

you = dict[user_choice]

print(f"computer chosse: {reverse_Dict[computer]}\nYou choose: {reverse_Dict[you]}")

if( computer == you):
    print("It's a tie!")

else:
  
  if( computer == -1 and you == 1):
    print("Congratulations! You Win.")
  elif( computer == -1 and you == 0):
    print("Computer Wins!")
  elif( computer == 1 and you == 0):
    print("Congratulations! You Win.")
  elif( computer == 1 and you == -1):
    print("Computer Wins!")
  elif( computer == 0 and you == -1):
    print("Congratulations! You Win.")
  elif( computer == 0 and you == 1):
    print("Computer Wins!")

  else:
    print("Something went wrong! Please try again.")