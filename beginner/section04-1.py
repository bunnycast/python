# 데이터 타입

v_str1 = "Bunnycast"
v_Bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "kim", 
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}


print(type(v_str1))
print(type(v_Bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))

i1 = 39 
i2 = 939
big_int1 = 99999999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2 )
print(f1 ** f2) # 제곱
print(f3 + i2) # 실수 + 자연수 > 실수 // 자동으로 형 변환이 이루어짐

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2, type(result2))

# 형변환
# int, float, complex(복소수)
print(int(result2))
print(float(c))
print(complex(3))
print(int(True)) # Boolean의 결괏값도 숫자로 형변환
print(int(False))
print(int('3')) # 문자 '3'도 숫자로 형변환
print(complex(False))

# 단항연산자
y = 100
y *= 100
print(y)

# 수치 연산 함수 (파이썬 연산 함수 공식 문서 링크)
print(abs(-7))
n, m = divmod(100, 8) # n/m 몫, 나머지 
print(n, m)

# math 패키지
import math
print(math.ceil(5.1))
print(math.floor(3.874))