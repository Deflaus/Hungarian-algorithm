from munkres import Munkres

matrix = [[5, 9, 1],
          [10, 3, 2],
          [8, 7, 4]]
m = Munkres()
indexes = m.compute(matrix)
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print('Работник ' + str(row) + ' - ' + str(column) + ' задача ( ' + str(value) + ' часов)')
    print(f'({row}, {column}) -> {value}')
print(f'total cost: {total}')
print('Все время - ' + str(total) + ' часов')
print(matrix)
