#boolean은 T/F을 나타내는 데이터 타입
print("Hello World!")


def say_hello(user_name, user_age):
  print("Hello",user_name, user_age, "how r you?")
  print("Hello", user_name, user_age, "how r you?")


#파이썬은 들여쓰기만 없으면 함수가 종료된 것으로 본다
say_hello("seongjae", 30)
#함수 안에 입력하는 데이터는 동작과 동시에 함수로 해당 데이터(인수,argument)를 보내는 것. 그러므로 함수에 그 데이터를 처리할 수 있는 공간(parameter,매개변수)이 있어야 정상 작동한다
say_hello("nico", 50)
say_hello("lynn", 32)


#print 순서대로 매개변수-인수가 1:1대응해야한다
def tax_caculator(money):
  print(money * 0.3)


tax_caculator(5000000)


#매개변수에 기본값이 있다면, 인수값이 주어지지 않아도 ok
def so_good(user_name="anoymous"):
  print("hello", user_name)


so_good()

def plus(a=0,b=0):
  print(a+b)
plus(3,6)
def minus(a=0,b=0):
  print(a-b)

minus(30,20)
def multifly(a=0,b=0):
  print(a*b)
def plus(a=0, b=0):
  print(a + b)


plus(3, 6)


def minus(a=0, b=0):
  print(a - b)


minus(30, 20)


def multifly(a=0, b=0):
  print(a * b)


multifly(40, 20)

multifly(40,20)
def divide(a=0,b=0):
  print(a/b)

divide(9,3)
def power_of(a=0,b=0):
def divide(a=0, b=0):
  print(a / b)


divide(9, 3)


def power_of(a=0, b=0):
  print(a**b)

power_of(2,5)

power_of(2, 5)


def tax_calc(money):
  return(money*0.35)
  return (money * 0.35)


#return은 값을 받아내고 보낼 수 있다, print는 콘솔에 출력만 할뿐



def pay_tax(tax):
  print("thank you for paying", tax)


to_pay = tax_calc(15000000)

pay_tax(to_pay)


def make_juice(fruit):
  return f"{fruit}+juice"


def add_ice(juice):
  return f"{juice}+ice"


def add_sugar(iced_juice):
  return f"{iced_juice}+sugar"


juice = make_juice("apple")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)
#파이썬에선 함수 안 return 밑의 코드는 작동하지 않는다

password_correct = False

if password_correct:
  print("Here is your money")
else:
  print("Wrong password")

winner = 10

if winner > 10:
  print("Winner is greater than 10")
elif winner < 10:
  print("Winner is less than 10")
else:
  print("Winner is 10")
#선순위 조건이 실행되면 나머지 조건문은 실행되지 않는다.

#CF(Control Flow): if, while
#bulitin function: 바로 사용가능한 함수들(standard library) 그 외엔 import 해올 것.

#list는 대괄호로 작성한다
days_of_week =["Mon","Tue","Wed","Thur","Fri"]

print(days_of_week)

name = "nico"
#.뒤 함수는 변수에 종속된 함수는 메서드!!! *함수 vs 메서드
print(name.upper())

#리스트 추가 시 맨 뒤로, 리스트 안에 리스트를 추가할 수 있

days = ["Mon","Tue","Wed"]
#튜플은 소괄, 불변, 메서드가 많지않음
#
print(days[-1])
#반대로 접근 가능하다(리스트, 튜플 모두), 튜플의 아이템에 접근할 때는 대괄호를 사용한다

#딕셔너리는 중괄호
player = {
  'name': 'nico',
  'age':'12',
  'alive': True,
  'fav_food' : ["pizza", "hambuger"]
}
#player라는 딕셔너리에 해당 속성들이 속한다는 개념

print(player.get('age'))

print
#리스트와 다르게 순서가 정해져 있지 않으므로 순서가 아니라 속성을 지정해서 추출할 수 있다.
"""
딕셔너리 데이터 변경방법
1. clear = 전부 삭제
2. pop = remove
player.pop('age')
3. 대괄호 = 새로 추가
player['xp'] = 1500
"""
#키 값으로는 문자열, 참거짓, 숫자, 리스트, 튜플이 사용가능
