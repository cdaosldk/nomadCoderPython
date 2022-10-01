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