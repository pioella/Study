print(abs(-3))
print(pow(2, 3))  # 2^3
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.99))
print("------------")
from math import *

print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))
print(ceil(5.00))
print("------------")

from random import *

print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))
print(int(random() * 10) + 1)

print(int(random() * 45) + 1)  # 1부터 46미만의 임의의 값 생성
print(randrange(1, 46))  # 1부터 46 미만의 임의의 값 생성
print(randint(1, 45))  # 1부터 45까지 임의의 값 생성

print(randint(1, 2))

# random 모듈의 shuffle과 sample
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
print(sample(lst, 2))
