# Section09
# 파일 읽기, 쓰기
# 읽기 : r, 쓰기 또는 삭제 : w, 파일 생성 또는 추가 : a
# 파이썬 공식 레퍼런스 주소 자료 참고

# 파일 읽기
# 예제 1 
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close로 리소스 반환! (중요)
f.close()

print("------------------------------------------")
print("------------------------------------------")

# 예제 2 - with문 open과 close를 동시 반환
with open('./resource/review.txt', 'r') as f:
  c = f.read()
  print(c)
  print(list(c)) # 리스트 형변환 가능
  print(iter(c)) # for 반복문 이터레이션 사용 가능

print("------------------------------------------")
print("------------------------------------------")

# 예제 3 
with open('./resource/review.txt', 'r') as f:
  for c in f:
    print(c.strip())

print("------------------------------------------")
print("------------------------------------------")

# 예제 4
with open('./resource/review.txt', 'r') as f:
  content = f.read()
  print(">", content)
  content = f.read() # 한번 돌아서 파일의 끝에 있기 때문에 내용 없음
  print(">>", content)

print("------------------------------------------")
print("------------------------------------------")

# 예제 5 - readline 한문장 단위로 읽어오기
with open('./resource/review.txt', 'r') as f:
  line = f.readline()
  # print(content)
  while line:
    print(line, end='')
    line = f.readline()

print()
print("------------------------------------------")
print("------------------------------------------")

# 예제 6 - readlines 리스트로 리턴함
with open('./resource/review.txt', 'r') as f:
  contents = f.readlines()
  print(contents)
  for c in contents:
    print(c, end='*************')

print()
print("------------------------------------------")
print("------------------------------------------")

# 예제 7 - 파일의 데이터 호출하여 평균값 구하기
score = []
with open('./resource/score.txt', 'r') as f:
  for line in f:
    score.append(int(line))
  print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제 1 
with open('./resource/text.txt', 'w') as f:
  f.write("Niceman! \n")

# 예제 2
with open('./resource/text.txt', 'a') as f:
  f.write("Goodman! \n")

# 예제 3
from random import randint

with open('./resource/text2.txt', 'w') as f:
  for cnt in range(6):
    f.write(str(randint(1,46)))
    f.write('\n')

# 예제 4 - writelines 리스트를 파일로 저장
with open('./resource/text3.txt', 'w') as f:
  list = ["kim \n", "Park \n", "Cho \n"]
  f.writelines(list)

# 예제 5 - 프린트 함수의 매개변수 file로 직접 파일에 텍스트 찍기 (예 : 로그파일)
with open('./resource/text4.txt', 'w') as f:
  print('Test Contents1!', file = f)
  print('Test Contents2!', file = f)