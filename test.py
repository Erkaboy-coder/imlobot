m = int(input('ustunlar sonini kiriting: \n'))
n = int(input('qatorlar sonini kiriting: \n'))

a = [list(map(int,input().split())) for i in range(n)]

sumRows = []

for i in range(n):
    sum = 0
    for j in range(m):
        sum += a[i][j]
    sumRows.append(sum/n)

result = max(sumRows)

for i in range(n):
    if sumRows[i] == result:
        print((i+1), "- maxsulot foydali")