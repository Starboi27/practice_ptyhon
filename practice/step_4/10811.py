"""
[] = 1, 2, 3, 4, 5
1) 2, 1, 3, 4, 5
2) 2, 1, 4, 3, 5
3) 3, 4, 1, 2, 5
2번 째 줄은 범위를 나타낸다
"""

n, m = map(int, input().split())
arr = list(range(1, n + 1))

for x in range(m):
    i, j = map(int, input().split())
    arr[i - 1 : j] = arr[i - 1 : j][::-1]

print(arr)

정리는 내일