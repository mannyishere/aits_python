# Read input which contains counting ceiling
f = open("countin.txt")
ceiling = [int(x) for x in f.readline().split()]
ceiling = ceiling[0]
f.close()

# Open output file
f = open("countout.txt", "w")

# Print out loop

for i in range(1, ceiling + 1):
    f.write(str(i)+"\n")

f.close()
