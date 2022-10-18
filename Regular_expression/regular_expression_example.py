import re
s='geeks.forgeeks'
match=re.search(r'.',s)
print(match)
# using \
match = re.search(r'\.', s)
print(match)
# A Python program to demonstrate working of
# findall()


# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)



# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))


# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already',
			flags=re.IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already'))

# As count has been given value 1, the maximum
# times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked already',
			count=1, flags=re.IGNORECASE))

# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',
			flags=re.IGNORECASE))
