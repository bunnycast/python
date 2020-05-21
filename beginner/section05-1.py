# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))
print()

# 예 if > 값이 참(true)일 경우 조건 실현 / Else > not if
if False:
    print("No")
else:
    print("Yes")
print()

# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print()

# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0

city = "1"
if city:
    print(">>>>True")
else:
    print(">>>>False")
print()

# 논리 연산자
# and or not
a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print(not False)
print(not True)
print()

# 산술, 관계, 논리 연산자
# 산술(+-*/) > 관계(><=) > 논리(and or not) 순서로 적용
print('ex1 : ', 5 + 10 > 0 and not 7 + 3 == 10) # 5+10이 0보다 큼 & 7+3이 10이 아니면 True / a-true , b-false > false

score1 = 90
score2 = 'A'

if score1 >=90 and score2 == 'A':
    print('합격하셨습니다.')    
else:
    print('죄송합니다. 불합격입니다.')
print()

# 다중조건문 if elif else
num = 76.7

if num >= 90:
    print("num 등급 A", num)
elif num >=80:
    print("num 등급 B", num)
elif num >=70:
    print("num 등급 C", num)
else:
    print("꽝")
print()

# 중첩조건문 if if if ... else
age = 27
height = 169

if age >= 20:
    if height >=170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")