from sys import argv

script, input_file = argv
#注意：python3中print（）带括号，f.read()也要有括号！
def print_all(f):
	print (f.read())
	
#定义函数后边要有冒号：，调用时不用
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print (line_count, f.readline())
	
current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)

print ("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)