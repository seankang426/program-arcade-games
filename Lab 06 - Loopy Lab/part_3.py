x = int(input('number input: '))
base = ' '
for i in range(x):
    base = ' '+ str(2 * (x - 1 - i) + 1) + base + str(2 * (x - 1 - i) + 1)+ ' '

length = len(base.strip())
graph = []
for j in range(x):
    line = ' '
    for k in range(j):
        line = ' ' + line + ' '
    for i in range(x    
