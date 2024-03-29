# Convert temperature from Celsius to Fahrenheit.
def convertTemp(c):
   f = (c * 1.8) + 32
   return f
cel = float(input("Temperature:"))
fahr = convertTemp(cel)
print(" The fahrenheit temperature of" , cel, "celcius is", fahr)
