N = int(input())

for i in range(N):
    n = int(input())
    if n == 0:
        del lst[-1]
    else:
        lst.append(n)
        
    
print(sum(lst))