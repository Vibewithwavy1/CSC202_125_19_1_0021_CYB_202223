#dictionaries
#empty dicitonary {}
#another example

student_scores = {
    "Henry": 81,
    "Peter": 95,
    "Mayor": 91,
    "Sandra": 74,
    "Naphthal": 88
}

student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades)
print(student_scores)

#dictionary inside dictionary
#nexted dict

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris","Lille","Dijon"], 
        "Total_visited": 12
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "Total_visited": 10
    },
]

print(travel_log)
    
    
