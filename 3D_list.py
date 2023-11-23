tables = []

for i in range(5):
    table = []
    for j in range(5):
        temp = []
        for k in range(5):
            temp.append(0)
        table.append(temp)
    tables.append(table)

table[3][3] = 1 # střed
for i in range(1, 4): # čtvrtá řada
    table[i][3] = 1
for i in range(5): # poslední řada
    table[i][4] = 1


columns = len(table)
rows = 0
if columns:
    rows = len(table[0])
for k in range (rows):
    for j in range(columns):
        print(table[i][j], end="")
        for i in range(columns):
         print(table[i][j][k], end="")
        print()




kinosaly[3][2][1] = 1