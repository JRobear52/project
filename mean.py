# Prints the mean of the numbers given as arguments
import sys

# Check for 'no argument' case and exit
if len(sys.argv) == 1:
	print 'Error: No arguments given.'
	sys.exit()

# This loop sums numbers in a file, only one number per line
sum = 0
n = 0
for num in open( sys.argv[1]):
    sum += float(num)
    n += 1

# this prints the mean value
print sum / n
