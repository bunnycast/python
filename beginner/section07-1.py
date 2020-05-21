# Section07-1 
# 파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명(첫글자는 대문자, 단어연결도 대문자):
#   함수
#   함수
#   함수


# 예제 1
class UserInfo:
  # 초기화, 속성, 메소드
  def __init__(self, name):
    self.name = name
  def user_info_p(self):
    print("Name : ", self.name)

user1 = UserInfo("Kim")
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# 예제 2
# self의 이해
class SelfTest:
  def func1():
    print('func1 called~!')
  def func2(self):
    print('func2 called~!')

self_test = SelfTest()

SelfTest.func1()
self_test.func2()

print(id(self_test))
SelfTest.func2(self_test)

# 예제 3
# 클래스 변수, 인스턴스 변수
class WareHouse:
  stock_num = 0
  def __init__(self, name):
    self.name = name
    WareHouse.stock_num += 1 
  def __del__(self):
    WareHouse.stock_num -= 1 

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__)
