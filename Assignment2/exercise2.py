# Function to filter and display employees with salary >= target salary
def display_employees(employee_list, target_salary):
    """
    Takes a list of employee tuples and a target salary.
    Displays employees with salary >= target_salary in a formatted table.
    """
    # Filter employees with salary >= target_salary
    # employee_list contains tuples in format (name, job, salary)
    filtered_employees = []
    for emp in employee_list:
        if emp[2] >= target_salary:  # emp[2] is salary
            filtered_employees.append(emp)
    
    # If no matches, print appropriate message
    if not filtered_employees:
        print(f"No employees found with salary >= {target_salary}")
        return
    
    # Sort by salary in descending order (largest first)
    # Sort by negative salary to get descending order
    filtered_employees.sort(key=lambda x: -x[2])
    
    # Display in a neatly formatted table
    print("\nEmployees with salary >= ", target_salary)
    print("-" * 50)
    # Print header
    print(f"{'Name':<20} {'Job':<20} {'Salary':>10}")
    print("-" * 50)
    
    # Print each employee
    for emp in filtered_employees:
        print(f"{emp[0]:<20} {emp[1]:<20} {emp[2]:>10}")
    
    print("-" * 50)


# ---------------- MAIN PROGRAM ----------------

# Ask user for file name
file_name = input("Enter the employee data file name: ")

# Attempt to open the file
try:
    file = open(file_name, "r")
except:
    # If file cannot be opened, output appropriate message and terminate
    print(f"Error: Cannot open file '{file_name}'")
    exit()

# Initialize list for employee tuples
employee_list = []

# Read each line and convert to tuple
for line in file:
    line = line.strip()  # Remove whitespace/newline
    if line:  # Skip empty lines
        # Split by comma
        name, job, salary_str = line.split(",")
        
        # Convert salary to integer
        salary = int(salary_str.strip())
        
        # Create tuple (name, job, salary) and add to list
        employee_tuple = (name.strip(), job.strip(), salary)
        employee_list.append(employee_tuple)

file.close()

# Output the list of tuples (no formatting required)
print("\nList of employee tuples:")
print(employee_list)

# Loop for salary queries
while True:
    print("\n" + "="*50)
    
    # Ask user to supply a salary
    salary_input = input("\nEnter a salary to search for (or 'q' to quit): ")
    
    # Check if user wants to quit
    if salary_input.lower() == 'q':
        print("Goodbye!")
        break
    
    # Convert input to integer
    try:
        target_salary = int(salary_input)
    except ValueError:
        print("Please enter a valid integer for salary.")
        continue
    
    # Call the function with employee list and target salary
    display_employees(employee_list, target_salary)
    
    # Ask if user wants to continue or quit
    continue_choice = input("\nWould you like to search with another salary? (y/n): ")
    if continue_choice.lower() != 'y':
        print("Goodbye!")
        break