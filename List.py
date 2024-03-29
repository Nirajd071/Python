courses=['History','Math','Physics',"computer"]
print(courses)
print(courses[2])#Physics
print(courses[-4])#History
#slicing
print(courses[0:3])#Range(includes first element and last-1)
courses.append('Chemistry')#adding element to list
print(courses)
courses.insert(2,'English')#inserting element to specific position
print(courses)
courses_2=['Biology','Zoology']
#add one list to another, but it adds whole list as one element
#courses.insert(2,courses_2)
print(courses_2)
#add element of one list to another list
courses.extend(courses_2)
print(courses)
#to remove only one elements from list
courses.remove('Math')
print(courses)

popped=courses.pop()
print(popped)
print(courses)



