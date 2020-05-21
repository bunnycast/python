# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서, 중복 X / 수정, 삭제 O - {}
# Key: Value (Json) -> MongoDB
# 선언
a = {'name': 'Kim', 'phone': '010-5012-8587', 'birth': 850903}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

# 출력
print(a['name'])
print(a.get('name')) # get 메소드 활용
print(a.get('address'))
print(c['arr'][1:3])
print()

# 딕셔너리 추가 - 순서가 섞일 수 있음
a['address'] = 'Seoul'
print(a)
a['rink1'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)
print()

# Keys + Values = items (중요)
print(a.keys())
print(list(a.keys())) # 키를 리스트로 형변환해야 인덱싱 가능!!

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items())) # 리스트 안에 key와 value가 튜플 형태로 반환

print()

print(2 in b)
print('name2' not in a)

print()
print()
print()

# 집합(sets) : 순서, 중복 X - set() 
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c) # 중복값 제외

t = tuple(b) # 튜플 형변환
print(t)

l = list(b) # 리스트 형변환
print(l)

print()
print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2)) # 교집합 검출
print(s1 & s2)

print()

print(s1 | s2) # 합집합 검출
print(s1.union(s2))

print()

print(s1 - s2) # 차집합 검출
print(s1.difference(s2))

print()

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
print(s3)

s3.remove(15)
print(s3)

print(type(s3))