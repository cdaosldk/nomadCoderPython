from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1,50)
playing = True

while playing:
  user_choice = int(input("choose number."))
  if user_choice == pc_choice:
    print("you won!")
    playing: False
  elif user_choice > pc_choice:
    print("lower!")
  elif user_choice < pc_choice:
    print("highter!")

