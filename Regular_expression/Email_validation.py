import email
import re

def validate_email(email):
# RegexObject = re.compile( Regular expression, flag )
# Compiles a regular expression pattern into
# a regular expression object
    regex_email = re.compile(r"""
                               ^([a-z0-9_\.-]+)                 # local Part
                               @                             # single @ sign
                                ([0-9a-z\.-]+)                 # Domain name
                               \.                             # single Dot .
                                ([a-z]{2,6})$                 # Top level Domain     
                               """, re.VERBOSE | re.IGNORECASE)
# RegexObject is matched with the desired
	# string using fullmatch function
	# In case a match is found, search()
	# returns a MatchObject Instance
    res=regex_email.fullmatch(email)
    if res:
        print("{} is valid, Details are as follows:".format(email) )
        # prints first part/personal detail of Email Id
        print("Local:{}".format(res.group(0)))

        # prints Domain Name of Email Id
        print("Domain:{}".format(res.group(1)))

        # prints Top Level Domain Name of Email Id
        print("Top Level domain:{}".format(res.group(2)))
        print()

    else:
        # If match is not found,string is invalid
        print("{} is Invalid".format(email))

validate_email("expectopatronum@gmail.com")
validate_email("avadakedavra@yahoo.com@")
validate_email("Crucio@.com")


def count_substring(string, sub_string):
    str1 = input()
    str_add = str1.__add__(str1)
    return


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)