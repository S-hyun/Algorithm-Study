import sys

num = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
x = int(sys.stdin.readline().strip())
arr.sort()

count = 0

left, right = 0, num-1
while(left < right):
    temp = arr[left] + arr[right]
    if temp == x:
        count = count + 1
        left = left + 1
        right = right -1
    elif temp > x:
        right = right -1
    elif temp < x:
        left = left + 1

print(count)
