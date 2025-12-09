from datetime import date

# Asking the user user to enter their date of birth in dd/mm/yyyy format
userDateOfBirth = input("Enter your date of birth (dd/mm/yyyy): ")

try:
    # Splitting the input string and converting day, month, and year into integers
    day, month, year = map(int, userDateOfBirth.split("/"))

    # Creating a date object for the user's date of birth
    DateOfBirth = date(year, month, day)
    
    # today's date
    today = date.today()
    
    # Checking if date is in the future
    if DateOfBirth > today:
        print("Error: Date of birth cannot be in the future.")
        exit()
    
    # Calculating age
    age = today.year - DateOfBirth.year
    

    if (today.month, today.day) < (DateOfBirth.month, DateOfBirth.day):
        age -= 1
    
    # Checking if today is birthday
    if today.day == DateOfBirth.day and today.month == DateOfBirth.month:
        print("Happy birthday!")
    
    # Checking if too young
    if age < 5:
        print("You're too young to use a computer")
    else:
        print(f"You are {age} years old.")

except ValueError:
     print("Error: Invalid date format or invalid date. Please use dd/mm/yyyy format.")