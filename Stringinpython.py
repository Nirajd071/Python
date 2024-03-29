message="malayalam"
print(message)
print(len(message))#To print lenght of string
print(message[6])#Accessing element in string
print(message[1:5])#string slicing
print(message.upper())#Using upper or lower case
print(message.count('a'))#To count total no of particular elements present in string
print(message.find('a'))#To find index of a first occuring element
new_message=message.replace('a','u')#To replace a word or character like in 3 idiot's movie
print(new_message)
greeting="Hello"
name="Niraj"
#message2=greeting +''+name +'.Welcome!'
#message2="{},{}.Welcome!".format(greeting,name)
message2=f"{greeting},{name}.Welcome!"
print(message2)
print(dir(message))#To know how many functions can be applied.
print(help(str.lower))
