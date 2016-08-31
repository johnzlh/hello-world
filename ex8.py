formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
	"I had this thing.", 
	"That you could type up right.", 
	"But it didn't sing.", 
	"So I said goodnight.")
)
#"But it didn't sing."中含有单引号，所以输出时只有这句用的是双引号

#Python objects (where feasible) attempt to represent themselves in a way that could be used to reconstruct the object exactly when using repr. Since your format string is %r rather than %s, you're asking for the string's repr instead of it's str representation. For strings with a single quote in them, there are a number of choices that would be valid repr representations.




#你应该看到的结果
#$ python ex8.py
#1 2 3 4
#'one' 'two' 'three' 'four'
#True False False True
#'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
#'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'