def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            ll = [l[i][0:3], l[i][3:6], l[i][6:9]]
            if l[i][0:3].startswith == 91:
                if len(l[i]) <= 10:
                    '+91', l[i][0:3]
                else:
                    '+', l[i][0:3]
            elif l[i][0:3].startswith == 0:    
                l[i][0:3].replace(l[i][0], '+') 
        return l
    return fun    

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

