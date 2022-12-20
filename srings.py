
print("Username format is (00year, initial, lastname, _S student, _T teacher, _A Admin staff).\n")
username = input('Enter your username: ')

if len(username) < 6 or "_" not in username:
    print("Enter a valid username.")
else:
    print(f'You are in year {username[0:2]}')
    print(f'Your name initial is {username[2:3]}')
    print(f'Your last name is {username[3:-2]}')
    
if username[-1] == "S":
    print("You ara a student.")
elif username[-1] == "T":
    print("You ara a Teacher.")
elif username[-1] == "A":
    print("You ara in Admin.")