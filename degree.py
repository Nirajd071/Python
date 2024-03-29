# Convert temperature from Celsius to Fahrenheit.
def convert(c):
    return 9/5 * c + 32
c=float(input("Enter a temperature in celcius degrees :"))
print("temperature in fahrenheit is", convert(c))