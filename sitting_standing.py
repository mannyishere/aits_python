# Open file
f = open("sitin.txt")

# Get inputs line by line. 
# First line contains hall dimension (x, y).
# Second line contains number of attendees (z).
# Converts both lists into integers
hall_dims = [int(x) for x in f.readline().split()]
numbers   = [int(x) for x in f.readline().split()]
# Close file
f.close()

# Calculates output values.
n_seats  = hall_dims[0] * hall_dims[1]
if numbers[0] <= n_seats:
    n_sitting  = numbers[0]
    n_standing = 0
else:
    n_sitting  = n_seats
    n_standing = numbers[0] - n_sitting

f = open("sitout.txt", "w")
f.write(str(n_sitting))
f.write(" ")
f.write(str(n_standing))
f.close()
