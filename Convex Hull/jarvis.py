
# Read file and discard the 3rd coordinate
rows =[]
with open("sample.txt") as f:
    lines = f.readlines()
    for line in lines:
        u = line.split()
        rows.append([u[0],u[1]])


