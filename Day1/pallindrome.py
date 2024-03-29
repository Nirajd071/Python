# to check if a given string is a pallindrome
def pallindrome(string):
    return string==string[::-1]

string=input("enter any string :")

if(pallindrome(string)):
    print(string,"is a pallindrome")
else:
    print(string,"is not a pallindrome")