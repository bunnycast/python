# Section04-2
# 문자열, 문자열 연산, 슬라이싱


str1 = "I am boy."
str2 = 'NiceMan'
str3 = ''
str4 = str('abc')

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab \t Tab"
print(escape_str2)

#  Raw String
raw_s1 = r'c:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티 라인
multi = \
""" 
문자열 
멀티라인 
테스트 
"""
print(multi)

# 문자열 연산
str_o1 = "*"
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "NiceMan"

print(str_o1 * 100) # *연산자는 반복
print(str_o2 + str_o3)
'''print(str_o1 + 3)'''
print()
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)
print()

# 문자열 형변환
print(str(77) + 'a')
print(str(10.4))
print()

# 문자열 함수 (문자열 활용 함수 링크 참조)
a = 'Niceman'
b = 'orange'

print(a.islower()) # 전부 소문자 검증
print(a.endswith('e')) # 끝글자 검사
print(b.endswith('e'))
print(a.capitalize()) # 첫글자 대문자 변환
print(a.replace('Nice', 'good')) # A를 B로 변환 (대소문자 구분)
print(list(reversed(b))) # 철자 역순(reversed)으로 list 형변환
print()

# 블록 후 전체 주석처리 Ctrl + /?
# 문자열 슬라이싱 (중요)
# 정방향은 0 부터, 역방향은 -1부터 

print(a[0:3])
print(a[0:4])
print(a[0:len(a)])
print(a[:4])
print(a[:])

print(b[0:4:2])
print(b[1:-2])
print(b[::-1])