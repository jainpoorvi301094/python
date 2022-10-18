calculation_to_seconds = 24 * 60 * 60  # Python variables defined dynamically
unit = "seconds"

def calculation(num_of_days):#def used to define function
    type_check=num_of_days>0  #it is a boolean type will return true or false
    print(type(type_check))  #This returns a type of the value
    return f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit}"



def validate():
    try:
        user_input_interger=int(num_of_days_list)
        if user_input_interger>0:
            number_of_seconds=calculation(user_input_interger)
            print(number_of_seconds)
        elif user_input_interger==0:
            print("you entered 0 please enter valid positive value")
        else:
            print("Entered negative number, no conversion for you!")
    except ValueError:
        print("enter a valid value")

user_input=""
while user_input!="exit":
    user_input = input("Please enter a value for days, so we can convert it into seconds")
    num_of_days_list1=user_input.split(",")
    print(num_of_days_list1)
    print(set(num_of_days_list1))

    #for num_of_days_list in user_input.split(","): This code is for LIST
    for num_of_days_list in set(num_of_days_list1): #This code is for set
        validate()


