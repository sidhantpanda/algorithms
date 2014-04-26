p = open("myfile.txt","w")

with open("sample.txt") as f:
    lines = f.readlines()
    for line in lines:
        u = line.split()
        p.write('['+str(u[0])+','+str(u[1])+'],\n')

p.close()