from datetime import datetime

current_year = datetime.now().year
birth_year = input("Enter your birth year: ")
age = current_year - int(birth_year)

print(age)
