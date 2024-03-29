#the compound interest for a given principal amount, interest rate, and time period
p=int(input("Enter principle amount :"))
r=float(input("Enter interest rate :"))
t=int(input("Enter time period :"))
n=int(input("How many times interest is compounded ? :"))
ci=p*pow((1+r/n),n*t)-p
print("compound interest is :",ci)