import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''

    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1
    
    if lower_count >= 1:
        strength += 1 
    if upper_count >= 1:
        strength += 1 
    if num_count >= 1:
        strength += 1 
    if wspace_count >= 1:
        strength += 1 
    if special_count >= 1:
        strength += 1 

    if strength == 1:
        remarks = "This Password Stinks! Change it NOW."
    elif strength == 2:
        remarks = "This Password SUCKS, Change it."
    elif strength == 3:
        remarks = "This Password is meh, change it."
    elif strength == 4:
        remarks = "This Password doesn't suck that much, it can be better."
    elif strength == 5:
        remarks = "Nice Password!"
    
    print('Your password has: ')
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password strength: {strength}")
    print(f"Hint: {remarks}")

def ask_pwd(another_pwd):
    if another_pwd:
        choice = input("Wanna try another password? (y/n): ").strip()
    else:
        choice = input("Do you want to check a password? (y/n): ").strip()
    while True:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            choice = input("What did you say? It's only supposed to be (y/n): ").strip()

if __name__ == '__main__':
    print("+++ Sup, welcome to my password checker +++")
    another = ask_pwd(False)
    while another:
        check_pwd()
        another = ask_pwd(True)


    


    
