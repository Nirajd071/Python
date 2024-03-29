courses=['History','Math','Physics','Computer']
for item in courses:
    print(item)
print("\n Elements of list with index ")
for index,course in enumerate(courses,start=1):
    print(index,course)
print("\n To print elements of list joined with string")
courses_str=' , '.join(courses)
newlist=courses_str.split(' , ')
print(courses_str)
print(newlist)