# Read input and format.
f = open("rainin.txt")
first_line = [int(x) for x in f.readline().split()]
n_data = first_line[0]
litres = first_line[1]
rain_preds = [int(x) for x in f.readlines()]
f.close()

# Set up loop
days = 0
litres_rain = 0

while litres_rain < litres:
    litres_rain += rain_preds[days]
    days += 1

# Write result to file
f = open("rainout.txt", "w")
f.write(str(days))
f.close()
