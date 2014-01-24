# variables
x = "there are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" % (binary, do_not)
# prints said text in " "
print x
print y

print "i said %r" % x
print "i also said '%s'." % y
#variables
hilarious = False
joke_evaluation = "isnt that joke so funny?! %r"
#prints the variables joke evaluation and hilarious
print joke_evaluation % hilarious
#variables
w = "this is the left side of..."
e = " a string with a right side."
# prints the variables above (w + e)
print w + e

