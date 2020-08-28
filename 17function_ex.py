def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("{:,}가 출금되었습니다.".format(money), "잔액은 {:,}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {:,}원입니다.".format(balance))
        return balance


def withdraw_night(balance, money): # 저녁에 출금, 수수료 발생
    commission = 100
    return commission, balance - money - commission


balance = 0
print("잔액은 {:,}원입니다.".format(balance))
balance = deposit(balance, 2200)
print("잔액은 {:,}원입니다.".format(balance))
balance = withdraw(balance, 1500)
print("잔액은 {:,}원입니다.".format(balance))
balance = withdraw(balance, 1000)
print("잔액은 {:,}원입니다.".format(balance))

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다다".format(commission, balance))

print()


# def profile(name, age, subject):
def profile(name, age=13, subject="수학"):
    print("이름 : {0},  나이 : {1},   좋아하는 과목 : {2}".format(name, age, subject))


profile("이재훈", 13, "수학")
profile("이재훈")
profile("이재훈", 14, "영어")
profile("이재훈", "영어")
profile(name="이재훈", age=15, subject="영어")
profile(name="이재훈", subject="영어")
profile("이재훈", subject="영어")

