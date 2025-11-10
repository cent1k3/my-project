n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))

matrix = []
print("Введите матрицу построчно:")
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

print("\nИсходная матрица:")
for row in matrix:
    print(" ".join(f"{x:.2f}" for x in row))





        
