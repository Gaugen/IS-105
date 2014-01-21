formatter = "%r %r %r %r" # makes formatter have a string with four inputs

print formatter % (1,2,3,4) # prints with selected variables
print formatter % ("one", "two", "three", "four")# prints with selected variables
print formatter % (True, False, False, True)# prints with selected variables
print formatter % (formatter, formatter, formatter, formatter) # prints with selected variables
print formatter % (
	"I had this thing.",
	"That u could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)# prints with selected variables
