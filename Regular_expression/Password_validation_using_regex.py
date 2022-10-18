import re
def main():
    password='@Geek123'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat=re.compile(reg)
    mat=re.search(pat,password)

    if mat:
        print("password is valid")
    else:
        print("Password is invalid")

if __name__=='__main__':
    main()