# str=input("enter any string :")[::-1]
# print(str)
# Function to reverse a string

def reverse(string):
	string = string[::-1]
	return string
s = input("what's string?")
print("The original string is : ", s)
print("The reversed string is : ", reverse(s))

    