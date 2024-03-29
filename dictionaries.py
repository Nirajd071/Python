student={'name':'niraj','age':25,'courses':['math','computer']}
print(student)
print("\n")
print(student['name'])
student['phone'] ='555-555'
student['name']='jane'
print(student.get('phone','Not found'))

student.update({'name':'niraj','age':26,'phone':'555-555'})
print(student)
del student['age']
print(student)
#popped method

courses=student.pop('courses')
print(student)
print(courses)