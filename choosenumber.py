from random import ranint

user_choice = int(input("choose number."))
pc_choice = randint(1,50)

if user_choice == pc_choice:
  print("you won!")
elif user_choice > pc_choice:
  print("lower!")
elif user_choice < pc_choice:
  print("highter!")

