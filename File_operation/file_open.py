'''file=open('sample.text','r')
#for each in file:
 #   print (each)
#print (file.read())
print (file.read(6)) #Another way to read a file is to call a certain number of characters'''
# Python code to illustrate split() function
with open("sample.text", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word)
