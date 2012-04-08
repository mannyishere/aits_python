# Set global constants
N_VILLAGERS = 11

# Read in input file containing the number of fruit on tak-tak tree at start
f = open("taktakin.txt")
n_fruit_0 = [int(x) for x in f.readline().split()]
f.close

# Now loop through months until the number of fruit (less one) is divisible
# by N_VILLAGERS

n_fruit = n_fruit_0[0]
n_months = 0

while (n_fruit - 1) % N_VILLAGERS != 0:
    n_fruit  *= 2 
    n_months += 1

# Now write results to file
f = open("taktakout.txt", "w")
f.write(str(n_months)+str(" ")+str(n_fruit))
f.close()
