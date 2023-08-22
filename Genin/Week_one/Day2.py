#Day 2
num = input("Enter any two digit number: ")
first = int(num[0])
second = int(num[1])
add = first + second
print(add)

#Mathematical operators PEMDAS
# + - * / **

#BMI Exercise
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
square_height = height ** 2
bmi = int(weight / square_height)
print("Your Body Mass Index is ", bmi)

#Rounding Numbers
print(round(8 / 3, 5))

#Exercise One
age = input("What is your current age? ")
years = 90 - int(age)
days = 365 *  int(years)
weeks = 52 * int(years)
months = 12 * int(years)
print(f"You have {days} days, {weeks} weeks and {months} months left ")

#Exercise - Tip Calculator
print("Welcome to the Tip Calculator")
total = float(input("What was the total bill? $"))
percentage = int(input("What percentage would you like to give? 10, 12 or 15? "))
people = int(input("How many people are to split the bill? "))
percentage_converted = percentage / 100 * total + total
each_person = round(percentage_converted / people, 2)
print("Each person should pay $",each_person)
