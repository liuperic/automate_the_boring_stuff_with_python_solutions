def column_widths(table):
    col_widths = [0] * len(table)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) > col_widths[i]:
                col_widths[i] = len(table[i][j])
    return col_widths

def print_table(table):
    col_widths = column_widths(table)
    for i in range(len(table[0])):  # number of rows
        for j in range(len(table)):     #number of columns
            print(table[j][i].rjust(col_widths[j]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)