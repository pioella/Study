from random import randint

number = 0
while number <= 10:
    print(number)
    number += 1

number = 0
quiz_number = randint(1, 100)

while number != quiz_number:
    number = int(input("숫자를 맞춰보세요 : "))
    if number > quiz_number:
        print(str(number) + "보다는 작습니다.")
    elif number < quiz_number:
        print(str(number) + "보다는 큽니다.")
    else:
        print("정답입니다.")

n = 0
while n >= 0:
    print(n)
    n += 1

