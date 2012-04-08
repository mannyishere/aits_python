# Read input. First line is number of data points. Subsequent lines are 
# data entries.
f = open("dishin.txt")
no_data  = [int(x) for x in f.readline().split()]
data_set = [int(x) for x in f.readlines()]
f.close()

# Calculate the statistics required and output.
f = open("dishout.txt", "w")
data_min  = str(min(data_set))
data_max  = str(max(data_set))
data_mean = str(int(sum(data_set) / no_data[0]))
f.write(data_min + " " + data_max + " " + data_mean)
f.close()

