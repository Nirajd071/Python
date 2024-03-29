#Mutable(can be modified)
list_1 = ['History','Math','Physics','Computer']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0]='Art'
print(list_1)
print(list_2)

#Immutable(can't be modified)
print("\n")
list_1 = ('History','Math','Physics','Computer')
list_2 = list_1
print(list_1)
print(list_2)
list_1[0]='Art'
print(list_1)
print(list_2)