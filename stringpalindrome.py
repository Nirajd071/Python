def isPalindrome(s):
	return s == s[::-1]
s = input("what's string?")
ans = isPalindrome(s)
if ans:
	print("Yes")
else:
	print("No")
