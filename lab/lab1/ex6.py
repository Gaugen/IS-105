x = "There are %d types of people." % 10 # defines variable
binary = "binary"# defines variable
do_not = "don't"# defines variable
y = "Those who know %s and those who know %s." % (binary, do_not)# defines variable 

print x # prints 
print y# prints

print "I said: %r." % x # prints and inserts the variable x
print "I also said: '%s'." % y # prints and inserts the variable y

hilarious = False # defines variable
joke_evaluation = "Isn't that a joke so funny?! %r" #defines variable with text string 

print joke_evaluation % hilarious # prints two variables

w = "This is the left side of..." # defines text string in variable
e = "a string with a right side." # defines text string in variable

print w + e # prints variable w and adds variable e.
