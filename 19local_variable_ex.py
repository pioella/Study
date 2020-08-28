# 지역 변수(local variable)와 전역 변수(global variable)

ball = 10


def playing(students):
    # ball = 20
    global ball
    ball = ball - students
    print("[함수 내] 남은 공 : {0}".format(ball))


def playing2(ball, students):
    ball = ball - students
    print("[함수 내] 남은 공 : {0}".format(ball))
    return ball


print("전체 공 : {0}".format(ball))
# playing(2)
ball = playing2(ball, 2)
print("남은 공 : {0}".format(ball))
