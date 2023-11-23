table= []
for j in range(5):
    column= []
    for i in range(5):
        column.append(0)
    table.append(column)

table[2][2] = 1 # střed
for i in range(1, 4): # čtvrtá řada
    table[i][3] = 1
for i in range(5): # poslední řada
    table[i][4] = 1

print(table)


