# defines function add so it adds
def add(a,b):
	print "Adding %d + %d" % (a, b)
	return a + b
# defines function subtract so it subtracts
def subtract(a, b):
	print "Subtracting %d - %d" % (a, b)
	return a - b
# defines function multiply so it multiplies 
def multiply (a, b) :
	print "Multiplying %d * %d" % (a, b)
	return a * b
# defnes function divide so it divides 
def divide (a, b) :
	print "Dividing %d / %d" % (a, b)
	return a / b
# prints text
print "Let's do som math with just functions!"
# defines variables
age = add(30, 5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)
# prints the variables
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway
print "Here is a puzzle."
# defines a variable with variables and functions inside which calculates
what = add (age, subtract(height, multiply(weight, divide(iq, 2))))
# prints text with variable inside.
print "That becomes: " , what, "Can you do it by hand?" 
