# Program to read a school username and determine the year group, initial, lastname, and role of the user

# Ask the user to enter their school username
username = input("Please enter your school username: ")

# Check if the username is less than 6 characters long or does not contain the character '_'
# If either of these conditions is true, ask the user to enter a valid username
if len(username) < 6 or '_' not in username:
    print("Please enter a valid username in the format: Year Group Initial Lastname _S/T/A")
else:
    # Split the username into its components
    year_group = username[:2]
    initial = username[2]
    lastname = username[3:-2]
    role = username[-2:]
    
    # Check if the user is a student or a member of staff
    if role == "_S":
        print("You are a student in year group " + year_group)
    else:
        print("You are a member of staff")
    
    # Display the initial and lastname of the user
    print("Your initial is " + initial)
    print("Your lastname is " + lastname)
    
    # Display the role of the user
    if role == "_S":
        print("You are a student")
    elif role == "_T":
        print("You are a teacher")
    elif role == "_A":
        print("You are an admin member of staff")
