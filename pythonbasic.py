#String Concatanation

print("number of days in month :"+str (30))
print(f"number of days in montn {30}")
#Variables
calculation_to_seconds=24*60*60 #Python variables defined dynamically
unit="seconds"
print(f"35 days are {35*calculation_to_seconds} {unit}")
print(f"40 days are {40*calculation_to_seconds} {unit}")
print(f"45 days are {45*calculation_to_seconds} {unit}") #f used for formating

#Function
def calculation(num_of_days, custom_message):#def used to define function
    type_check=num_of_days>0  #it is a boolean type will return true or false
    print(type(type_check))  #This returns a type of the value
    if(num_of_days>0):
        print(f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit}")
        print(custom_message)
    elif num_of_days==0:
        print("you entered 0 please enter valid positive value")
    else:
        print("You entered negative value")

calculation(39, "Awesome")
calculation(48,"looks good")
calculation(82, "great")

def scope_check(num_of_days):
    print(calculation_to_seconds)  # global variable
    print(num_of_days) #Internal variable by parameter
    year=2012
    print(year)  #Internal variable


scope_check(30)
user_input=input("please enter a number")  #Input function used to get input from the user
print(user_input)
user_input_to_integer=int(user_input)
calculation(user_input_to_integer, "great")


#Function with return type
def calculation(num_of_days, message):   #def used to define function
    print(message)
    return f"{num_of_days} days are {num_of_days*calculation_to_seconds} {unit}"



number_of_seconds=calculation(39, "I am function with return")
print(number_of_seconds)
