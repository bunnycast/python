# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제 1
with open('./resource/sample1.csv', 'r') as f:
  reader = csv.reader(f)
  # next(reader) - 1행(헤더) 스킵
  # 확인
  print(reader)
  print(type(reader))
  print(dir(reader))

  for c in reader:
    print(c)

# 예제 2 - delimiter 구분자 지정 옵션
with open('./resource/sample2.csv', 'r') as f:
  reader = csv.reader(f, delimiter = '|')
  # next(reader) - 1행(헤더) 스킵
  # 확인
  print(reader)
  print(type(reader))
  print(dir(reader))

  for c in reader:
    print(c)

# 예제 3 (dict 변환)
# 예제 1
with open('./resource/sample1.csv', 'r') as f:
  reader = csv.DictReader(f)

  for c in reader:
    for k, v in c.items():
      print(k, v)

# 예제 4
w = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18]]

with open('./resource/sample3.csv', 'w', newline='') as f:
  wt = csv.writer(f)

  for v in w:
    wt.writerow(v)

# 예제 5 - writerows, writerow 이터레이션 함수
with open('./resource/sample4.csv', 'w', newline='') as f:
  wt = csv.writer(f)
  wt.writerows(w)
print('----------------------------')
print()

# XSL, XSLX
# openpyxl, xlswriter, xlrd, xlwt, xlutils 등의 엑셀 파일 관리 오픈소스 유틸이 다양함 
# pandas 를 주로 사용

import pandas as pd

# sheetname='시트명' or 숫자, header=숫자, skiprow=숫자 pandas excel
xlsx = pd.read_excel('./resource/sample.xlsx')

print('----------------------------')
print()

# 상위데이터(상단 5행 데이터) 확인
print(xlsx.head())

print('----------------------------')
print()

# 하위 데이터(하단 5행 데이터) 확인 
print(xlsx.tail())

# 데이터 구조(행, 열) 확인
print(xlsx.shape)

# 엑셀 or csv 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)