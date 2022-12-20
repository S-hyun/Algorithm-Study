import sys
import math
num = int(sys.stdin.readline().strip())

arr = [0 for i in range(10)]
for i in str(num):
    arr[int(i)] = arr[int(i)]+1
    
arr[6] = math.ceil((arr[6] + arr[9]) / 2)
arr[9] = 0

print(max(arr))
