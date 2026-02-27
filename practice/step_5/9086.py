t = int(input())

a = []
for x in range(t):
    a.append(input())

for x in range(t):
    print(a[x][0] + a[x][len(a[x]) - 1])
