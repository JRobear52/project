# Prints the mean of the numbers given as arguments
import sys

# Check for 'no argument' case and exit
if len(sys.argv) == 1:
	print 'Error: No arguments given.'
	sys.exit()

# This loop sums the arguments
sum = 0
for num in sys.argv[1:]:
    sum += float(num)

# this prints the mean value
print sum / (len(sys.argv) - 1)
