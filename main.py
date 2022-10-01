#파이썬 스타일:스네이크케이스
#변수는 숫자로 시작하면 안된다
#boolean은 T/F을 나타내는 데이터 타입
print("Hello World!")

def say_hello(user_name, user_age):
  print("Hello",user_name, user_age, "how r you?")
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

multifly(40,20)
def divide(a=0,b=0):
  print(a/b)

divide(9,3)
def power_of(a=0,b=0):
  print(a**b)

power_of(2,5)

def tax_calc(money):
  return(money*0.35)
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