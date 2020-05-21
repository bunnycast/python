# Section05-2
# 파이썬 흐름 제어 (반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is :", v2)

for v3 in range(1,11):
    print("v3 is :", v3)

# 1부터 100까지 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print("1 ~ 1999 : ", sum1)
print("1 ~ 1999 : ", sum(range(1, 101)))
print("1 ~ 1999 : ", sum(range(1, 101, 2))) # 1~100까지 두개 단위 건너뛰면서 계산
print()

# 시퀀스(순서가 있는) 자료형 반복 (중요)
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable : range, reversed, enumerate, filter, map, zip

# 리스트 
names = ["Kim", "Park", "Cho", "Choi", "Yoo"]
for Y in names:
    print("Yor are : ", Y)
print()

# 문자열
word = "dreams"
for s in word:
    print("Word : ", s)
print()

# 딕셔너리
my_info = {
    "name" : "Kim",
    "age" : 33,
    "city" : "Seoul"
}

for key in my_info: # 기본값은 키 
    print("my_info : ", key)

for key in my_info.keys(): # 키
    print("my_info : ", key)

for v in my_info.values(): # 밸류
    print("my_info : ", v)

for k, v in my_info.items(): # 아이템 (키 + 밸류)
    print("my_info : ", k, v)
print()

# for 반복문을 활용한 대소문자 전환
name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())
print()

# break - for문 반복 중 원하는 답을 찾을 경우 반복 중단 
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 24, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break 
    else:
        print("not found : 33!")
print()

# for else 구문 - 반복문이 정상적으로 수행된 경우(break 작동 X) else 블럭 수행
for num in numbers:
    if num == 373:
        print("found : 373!")
        break 
    else:
        print("not found : 373!")
else:
    print("not found 373...........")
print()

# continue
lt = {"1", 2, 5, True, 4.3, complex(4)}

for v in lt:
    if type(v) is float:
        print(v, "찾았따!")
        continue
    print("타입 : ", type(v))
print()

name = "Niceman"
print(reversed(name))
print(set(reversed(name)))