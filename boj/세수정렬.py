import sys
score_str = sys.stdin.readline().strip().split()
score = [int(i) for i in score_str]
score.sort()
for i in score:
    print(i, end=' ')
