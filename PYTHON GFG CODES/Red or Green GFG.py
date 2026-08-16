s = "R"

G_count = 0
R_count = 0

for char in s:
    if char == 'G':
        G_count += 1
    else:
        R_count += 1

print(min(G_count, R_count))

