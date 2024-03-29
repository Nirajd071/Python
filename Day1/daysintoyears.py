# Python Program to Convert Days into Years, Weeks, and Days
print("Enter the Number of Days:", end=" ")
num = int(input())

year = int(num / 365)
week = int((num % 365) / 7)
days = int((num % 365) % 7)

print("\nYear:", year, ", Week:", week, ", Day:", days)
