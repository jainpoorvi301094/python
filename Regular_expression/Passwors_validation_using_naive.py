# Password validation in Python
# using naive method

# Function to validate the password

def passwd_check(passwd):
    specialSym=['$','@','#','%','!']
    value=True

    if(len(passwd)<6):
        print("Please enter minimum eight digit password")
        value=False

    if(len(passwd)>16):
        print("password length should be between 8-16")
        value = False

    if not any(char.isdigit() for char in passwd):
        print("Password should have one numeric value")
        value = False

    if not any(char.isupper() for char in passwd):
        print("Password should have one Uppercase letter")
        value = False

    if not any(char.islower() for char in passwd):
        print("Password should have a lowecase letter")
        value = False

    if not any(char in specialSym for char in passwd):
        print("password should contain any special character")
        value = False

    if value:
        return value

def main():
    passwd="Geek12@e"
    if(passwd_check(passwd)):
        print("password is valid")
    else:
        print("password is invalid")

if __name__=='__main__':
    main()
