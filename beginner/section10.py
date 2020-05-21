# Section10
# 파이썬 예외 처리의 이해

# 예외 종류
# 문법적으로 예러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크 

# SyntaxError : 잘못된 문법
# print('test)
# if True
#  pass
# x => y  


# NameError : 참조변수 없음
a = 10
b = 25
#print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
# x = [10, 20, 30]
# print(x[3])

# KeyError - get 메소드로 해결
dic = {'name' : 'kim', 'Age' : '33', 'City' : 'Seoul'}
# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 없는 속성 사용시에 예외
import time
print(time.time())
# print(time.month())

# ValueError : 참조값이 없을 경우
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError : 외부 파일 처리시 파일 경로가 잘못된 경우
# f = open('test.txt', 'r')

# TypeError : 자료형이 맞지 않는 데이터의 결합, 형번환으로 해결
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(X + z)
print(x + list(y))


# 항상 예외가 발생하니 않을 것으로 가정하고 먼저 코딩
# 런타임 예외 발생 시 예외 처리 코딩 권장(EAFP)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않을 경우 실행
# finally : 항상 실행

# 예제 1 
name =['kim', 'lee', 'park']

# try :
#   z = 'kim'
#   x = name.index(z)
#   print('{} Found it! in name'.format(z, x+1))
# except ValueError:
#   print('Not found it! - Occured ValueError!')
# else:
#   print('OK! else!')

# 예제 2 - 어떤 에러가 나올지 모를 때
name =['kim', 'lee', 'park']

# try :
#   z = 'kim'
#   x = name.index(z)
#   print('{} Found it! in name'.format(z, x+1))
# except:
#   print('Not found it! - Occured Error!')
# else:
#   print('OK! else!')

# 예제 3 - finally 무적권
name =['kim', 'lee', 'park']

# try :
#   z = 'kim'
#   x = name.index(z)
#   print('{} Found it! in name'.format(z, x+1))
# except:
#   print('Not found it! - Occured Error!')
# else:
#   print('OK! else!')
# finally:
#   print('finally OK!')

# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
  print('Try')
finally:
  print('ok Finally!!!')

# 예제 5 - 중첩 에러 검사, exception이 맨 마지막으로
name =['kim', 'lee', 'park']

# try :
#   z = 'cho'
#   x = name.index(z)
#   print('{} Found it! in name'.format(z, x+1))
# except ValueError as l:
#   print(l)
# except IndexError:
#   print('Not found it! - IndexError Error!')
# except Exception:
#   print('Not found it! - Occured Error!')
# else :
#   print('OK! else!')
# finally:
#   print('finally OK!')

# 예제 6 
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try: 
  a = 'choi'
  if a == 'kim':
    print('OK 허가!')
  else:
    raise ValueError
except ValueError:
  print('문제 발생!')
except Exception as f:
  print(f)
else:
  print('OK!')