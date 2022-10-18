import datetime

target_input=input("Enter your target detail\n")
input_list=target_input.split(":")
print(input_list)

goal=input_list[0]
deadline=input_list[1]

deadline_date=datetime.datetime.strptime(deadline, "%d.%m.%Y")
print(deadline_date)
today=datetime.datetime.today()
print(today)

time_till_deadline=deadline_date-today
print(f"Dear user time for your goal to learn {goal} is remaining {time_till_deadline.days} days")


