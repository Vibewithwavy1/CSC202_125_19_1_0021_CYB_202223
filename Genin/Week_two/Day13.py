#take input and output
year = int(input("What is your of birth?: "))
if year > 1989 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z. ")
        
#another one 
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can not drive at {age}years grow to 18")
       
#take another input
pages = 0
word_per_page = 0
pages = int(input("Number of page: "))
word_per_page =  int(input("Number of words page page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)