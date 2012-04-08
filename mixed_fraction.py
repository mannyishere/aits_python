# Open file. Read in line with numerator and denominator (x, y)
f = open("mixin.txt")
# Convert inputs into integers.
numbers = [int(x) for x in f.readline().split()]
f.close()
# Determine whole and fractional part of mixed fraction
fractional_part = numbers[0] % numbers[1]
whole_part = int((numbers[0] - fractional_part) / numbers[1])
# Write out into file
f = open("mixout.txt", "w")
f.write(str(whole_part))
if fractional_part != 0:
    f.write(str(" "))
    f.write(str(fractional_part)+"/"+str(numbers[1]))
f.close()
