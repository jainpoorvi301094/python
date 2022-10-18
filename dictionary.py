
def calculation(num_of_days, calculation_unit):#def used to define function
    type_check=num_of_days>0  #it is a boolean type will return true or false
    print(type(type_check))  #This returns a type of the value
    if calculation_unit=="hours":
        return f"{num_of_days} days are {num_of_days*24} hours"
    elif calculation_unit=="minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit"




def validate():
    try:
        user_input_interger=int(days_and_unit_dictionary["days"])
        if user_input_interger>0:
            number_of_seconds=calculation(user_input_interger,days_and_unit_dictionary["unit"])
            print(number_of_seconds)
        elif user_input_interger==0:
            print("you entered 0 please enter valid positive value")
        else:
            print("Entered negative number, no conversion for you!")
    except ValueError:
        print("enter a valid value")

user_input=""
while user_input!="exit":
    user_input = input("Please enter a value for days and conversion unit \n")
    days_and_unit=user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary={"days":days_and_unit[0],"unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))  #Nested Function
    validate()



