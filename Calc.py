import sys

number = sys.argv[1]
sign = sys.argv[2]
number2 = sys.argv[3]
calc = 0

#print(type(number))
#print(type(number2))
#print(type(sign))

#Addition
if(sign == '+'):
	calc = int(number) + int(number2)

#Subtraction
if(sign == '-'):
	calc = int(number) - int(number2)

#Multiplication
if(sign == '*'):
	calc = int(number) * int(number2)

#Division
if(sign == '/'):
	calc = int(number)/int(number2)

#Output
print(number + sign + number2)
print(calc)