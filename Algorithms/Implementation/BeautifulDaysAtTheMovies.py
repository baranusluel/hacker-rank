i,j,k = [int(tmp) for tmp in input().strip().split(' ')]
days = range(i, j+1)
beautiful = 0
for day in days:
    if abs(day - int(str(day)[::-1])) % k == 0:
        beautiful += 1
print(beautiful)