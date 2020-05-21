# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트(순서, 중복, 수정, 삭제 모두 가능) - []
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pen', 'banana', 'orange']
e = [10, 100, ['pen', 'banana', 'orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])
print()

# 슬라이싱
print(d[0:2])
print(e[2][1:3])
print()

# 연산
print(d + c)
print(c * 3)
print(str(c[0])+'hi')
print()

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()

# 리스트함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2, 7)
print(y)
y.remove(2) # 데이터의 값을 찾아 삭제 cf. remove - del - pop
y.remove(7)
print(y)
y.pop() # Last In First Out
print(y)
ex = [88, 77]
y.extend(ex) # 88,77
# y.append(ex) # [88,77]
print(y)
print()
print()
print()

# 튜플 (순서, 중복 O / 수정, 삭제 X) - 변경되면 큰일나는 중요 데이터 () 
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)
print()

# 튜플 함수
z = (5, 2, 1, 3, 4)

print(z)
print(3 in z)
print(z.index(5)) # 값이 있는 인덱스(위치) 반환
print(z.count(1)) # 값이 있는 인덱스 갯수