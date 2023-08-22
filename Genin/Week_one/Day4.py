#Day 4 -Randomization and Python Lists

#Randomization 
import random
random_integer  = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)
print(random_float * 5)

#Day 4.1 Heads or Tails Exercise
import random
random.seed()
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
random_int = random.randint(0, 1)
if random_int == 1:
    print("Heads")
else:
    print("Tails")

#4.2 Banker Roulette - Who will pay the bill?
import random
random.seed()
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("Give me everybody's names, separated by a comma. ")
names = namesAsCSV.split(", ")
person_who_pays = random.choice(names)
print(person_who_pays, "will be paying for the meal")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

#Day 4.3 -Treasure Map/
row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to place the treasure? ")

horizontal_position = int(position[0])
vertical_position = int(position[1])
selected_row = map[vertical_position - 1]
selected_row[horizontal_position - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")

#Day 4.4 A Rock, Paper and Scissors Game
import random
user_choice = int(input("What do you choose? Type  0 for rock, 1 for paper and 2 for scissors \n"))
computer_choice = random.randint(0, 2) 
print(f"The computer chooses {computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("You type an invalid command. You lose") 
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == computer_choice:
    print("It is a draw")
else:
    print("You type an invalid number. You lose")

