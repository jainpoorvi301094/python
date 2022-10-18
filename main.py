#import helper_main
#If we want to fetch specific function the we will use below syantax
#from helper_main import * This will import everything from module. The difference is import helper_main is the syntax.
#import helper_main as h

from helper_main import validate, user_input_message
user_input=""

while user_input!="exit":
    user_input = input(user_input_message)
    days_and_unit=user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary={"days":days_and_unit[0],"unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))  #Nested Function
    #helper_main.validate(days_and_unit_dictionary)  When we import helper_main
    # h.validate(days_and_unit_dictionary)  When we import helper_main as h
    validate(days_and_unit_dictionary) # from helper_main import validate
