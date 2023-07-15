"""yапишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и 
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, 
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой 
ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y)"""

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    matrix = [[0] * 6 for _ in range (6)]
    for i in range(6):
        for j in range(6):
            matrix [i][j] = (i + 1) * (j + 1)
        for row in matrix:
            for elem in row:
                print(elem, end = ' ')
            print()


print_operation_table(lambda x, y: x * y)