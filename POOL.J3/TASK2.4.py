# TASK 2.4
# Can you predict the result of the following snippet of code?
# [::-2] = jhfdb(shows every 2nd index from back to start)
# [:5] = jhfdb (from index 0 to the 4th)
# [::-1] = bdfhj (from index -1 to the end: it's reversed)
# [3:] = hj (from index 3 to the end)

p = "abcdefghij"
print(p[::-2][:5][::-1][3:])

# TASK 2.5
# Can you break down each step in order to simplify the previous code?
print(p[::-2])
print(p[::-2][:5])
print(p[::-2][:5][::-1])
print(p[::-2][:5][::-1][3:])