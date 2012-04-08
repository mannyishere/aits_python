# Read inputs. Two lines of [(x1,y1), (x2,y2)] coords representing
# top left and bottom right coords. Convert to integers.
f = open("bendin.txt")
r1 = [int(x) for x in f.readline().split()]
r2 = [int(x) for x in f.readline().split()]
f.close()

# Calculate total area, ignoring overlapping region
total_area = ((r1[2] - r1[0]) * (r1[3] - r1[1]) + 
              (r2[2] - r2[0]) * (r2[3] - r2[1]))
overlap_area = (max((min([r1[2], r2[2]]) - max([r1[0], r2[0]])), 0) * 
                max((min([r1[3], r2[3]]) - max([r1[1], r2[1]])), 0))
spanned_area = total_area - overlap_area

# Write result into file
f = open("bendout.txt", "w")
f.write(str(spanned_area))
f.close()

