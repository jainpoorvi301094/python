import json
person = {"name":"poorvi", "age":27, "city":"Indore", "titles":"Engineer"}
person_json = json.dumps(person, indent=4, sort_keys=True)
#print(person_json)

#with open('person_json', 'w') as file:  # Convert dictionary to json file
  #  json.dump(person, file, indent=4)

#Decode Json file
with open('person_json', 'r') as file:
    person = json.load(file)
    print(person)