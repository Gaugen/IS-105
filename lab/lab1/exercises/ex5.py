name = 'Zed A. shaw'
age = 35 # not a lie
height = 74 * 2.54 # inches * 2.54 = centimeters
weight = 180 * 2.2# lbs * 2.2 is kilo
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilos heavy." % weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get is exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
