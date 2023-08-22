#Day 5 - Loops, Range and Code Block

#Exercise - Average Height Exercise

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print("The watermelon is outside the for loop")

#Average Height Exercise
student_heights = input("Input the list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0 
for height in student_heights:
    total_height += height
print(total_height)

num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(num_of_students)

average_height = round(total_height / num_of_students)
print(average_height)

#Highest Score
student_scores = input("Input the list of student heights ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")

#Range
total = 0
for number in range (1, 101):
    total += number
    print(total)

#AddingEvens Exercise
total = 0
for number in range (0, 101):
    if number % 2 == 0:
        total += number
        print(total)

#FizzBuzz Game
print("Welcome to FizzBuzz Game")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else:
        print(i)

#PyPassword Generator
import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', ' 3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
nr_alphabets = int(input("How many letters would you like in your password? \n"))
nr_numbers = int(input("How  many numbers would you like? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))


password = ""
for char in range(1, nr_alphabets + 1):
    password += random.choice(alphabets)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
print(password)


password_list = []
for char in range(1, nr_alphabets + 1):
    password_list.append(random.choice(alphabets))

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
   
print(password_list)
random.shuffle(password_list)
print(str(password_list))

password = ""
for char in password_list:
    password += char
print(password) 