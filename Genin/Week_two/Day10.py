#Day10 - functions with output
#change the title of your string

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    print(f_name.title())
    print(l_name.title())
fi_name = input("Enter your first name: ")
li_name = input("Enter your last name: ")

format_name(fi_name, li_name)
print(len(fi_name))
print(len(li_name))

#leap year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print(" Not leap year.")
leap_month = 29
        
def days_in_months(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        print(leap_month)
    else:
        return month_days[month - 1 ]
        
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_months(year, month)
print(days)