# Read in file addin.txt and return sum of two numbers.
# Spec: addin.txt has one line with two numbers separated by a space.

first_line = open("addin.txt").readline().split()
numbers = [int(x) for x in first_line]
sum_values = str(sum(numbers))
open("addout.txt", "w").write(sum_values)