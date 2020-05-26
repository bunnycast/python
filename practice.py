import sys

N = int(input())

stk = []
for i in range(N):
    k = int(input()) # 인수 입력
    for _ in range(k):
        while _ + 1 <= k:
            stk.append(_ + 1)
        if stk[-1] = k: # push
            print("+")
            print(stk)
        elif stk[-1] == k: # pop
            print('+')
            print(stk)
            stk.pop()
            print("-")
            print(stk)
        elif stk[-1] > k: # i > k "NO"
            print("NO")
        else:
            pass