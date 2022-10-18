calculation_to_seconds = 24 * 60 * 60  # Python variables defined dynamically
unit = "seconds"

def calculation(num_of_days):#def used to define function
    type_check=num_of_days>0  #it is a boolean type will return true or false
    print(type(type_check))  #This returns a type of the value
    return f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit}"


user_input=input("Please enter a number")

def validate():
    if user_input.isdigit():
        user_input_interger=int(user_input)
        if user_input_interger>0:
            number_of_seconds=calculation(user_input_interger)
            print(number_of_seconds)
        elif user_input_interger==0:
            print("you entered 0 please enter valid positive value")
    else:
        print("enter a valid value")

validate()


