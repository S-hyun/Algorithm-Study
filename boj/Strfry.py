import sys

num = int(sys.stdin.readline().strip())
for i in range(num):
    A, B = sys.stdin.readline().strip().split()
    arr_A = [0 for i in range(ord('z')-ord('a')+1)]
    for i in A:
        arr_A[ord(i)-ord('a')] = arr_A[ord(i)-ord('a')]+1
    arr_B = [0 for i in range(ord('z')-ord('a')+1)]
    for i in B:
        arr_B[ord(i)-ord('a')] = arr_B[ord(i)-ord('a')]+1
    if arr_A == arr_B:
        print("Possible")
    else:
        print("Impossible")

