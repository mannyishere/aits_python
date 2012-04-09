# Read input and process.
f = open("encyin.txt")
in_params = [int(x) for x in f.readline().split()]
pages_ency = in_params[0]
number_qs  = in_params[1]
# Read in remaining info
in_other = [int(x) for x in f.readlines()]
f.close()
# Split list
words_on_page = in_other[0:pages_ency]
pages_sought  = in_other[pages_ency:(pages_ency + number_qs)]

# Find number of pages and write to file
f = open("encyout.txt", "w")
for i in pages_sought:
    f.write(str(words_on_page[i - 1]) + "\n")
f.close()
