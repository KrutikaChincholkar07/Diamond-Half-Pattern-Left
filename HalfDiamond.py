rows = 4

# Upper half
for i in range(1, rows + 1):
    print("* " * i)

# Lower half
for i in range(rows - 1, 0, -1):
    print("* " * i)
