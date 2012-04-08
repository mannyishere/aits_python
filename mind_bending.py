# Read inputs. Two lines of [(x1,y1), (x2,y2)] coords representing
# top left and bottom right coords. Convert to integers.
f = open("bendin.txt")
r1 = [int(x) for x in f.readline().split()]
r2 = [int(x) for x in f.readline().split()]
f.close()

# Calculate total area, ignoring overlapping region
total_area = ((r1[2] - r1[0]) * (r1[3] - r1[1]) + 
              (r2[2] - r2[0]) * (r2[3] - r2[1]))

# Calculate spanned area, without double counting overlap where necessary.
# Overlap does not occur when right-edge of one rectangle is less than the
# left-edge of the other rectangle - irrespective of vertical position.
# Alternatively overlap does not occur when top-edge of one rectangle is 
# less than the bottom-edge of the other rectangle - irrespective of 
# horizontal position.

# Right edge is less than left edge.
is_x_overlap = (r1[2] > r2[0]) or (r2[2] > r1[0])
# Top edge is less than bottom edge.
is_y_overlap = (r1[3] < r2[1]) or (r2[3] < r1[1])

if not (is_x_overlap or is_y_overlap):
    spanned_area = total_area
else:
    overlap_area = (max((min([r1[2], r2[2]]) - max([r1[0], r2[0]])), 0) * 
                    max((min([r1[3], r2[3]]) - max([r1[1], r2[1]])), 0))
    spanned_area = total_area - overlap_area

# Write result into file
f = open("bendout.txt", "w")
f.write(str(spanned_area))
f.close()

