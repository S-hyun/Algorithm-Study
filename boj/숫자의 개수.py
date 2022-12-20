import sys
A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
mult = A * B * C

mult_str = str(mult)
arr = [0 for i in range(10)]
for i in mult_str:
    arr[int(i)] = arr[int(i)]+1
for i in arr:
    print(i)
