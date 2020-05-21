# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k in q1.keys():
    if k == '가을':
        print("1. ", q1[k])

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for k, v in q2.items():
    if v == "사과":
        print("2. ", k, v)
        break
else:
    print("2. 사과 없음")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 76.7

if score >= 81:
    print("3. A학점")
elif score >=61:
    print("3. B학점")
elif score >=41:
    print("3. C학점")
elif score >=21:
    print("3. D학점")
else:
    print("3. E학점")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18

best = a

if b > a:
    best = b
if c > b:
    best = c
print("4. ", best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
z = '891002-47837'

if int(z[7]) == 1 or int(z[7]) == 3:
    print("남자")
elif int(z[7]) == 2 or int(z[7]) == 4:
    print("여자")
else:
    print("외계인")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:
    if v == "정":
        continue
    else:
        print(v, end='')
print()

# 리스트 컴프리헨션
q5 = [v for v in q3 if v != '정']
print(q5)
print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for v7 in range(1,100):
    if v7 % 2 != 0:
        print(v7, end=',')
print()

# 리스트 컴프리헨션
q6 = [x for x in range(1, 101) if x % 2 == 1]
print(q6)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for z in q4:
    if len(z) >= 5:
        print(z, end=',')
print()

word = [w for w in q4 if len(w) >= 5]
print(word)

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for n in q5:
    if n.isupper():
         continue
    else:
        print(n, end=',')
print()

alp = [c for c in q5 if c.islower()]
print(alp)

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for n in q6:
    if n.isupper():
        print(n.lower(), end=',')
    else:
        print(n.upper(), end=',')
print()

# 리스트 컴프리헨션 - 리스트를 쉽게 만드는 방법
number = [n for n in range(1, 101)]
print(number)
print()

for n in range(1, 101):
    number.append(n)
print(number)
print()

for n in range(1, 101):
    n += 1
print(number)