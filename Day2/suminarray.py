num=[1,2,3,4,5,6,7,8,9,98,76,54,34,21]
sum=0;
for i in range(len(num)):
    print(num[i])
    sum=sum+num[i]
print("================================")
print("The sum of numbers in list are:",sum)
avg=sum/len(num)

print("the average is :",avg)