#가변인자
# def profile(name, age, subject1, subject2, subject3, subject4, subject5):
#     print("이름 : {0},  나이 : {1},".format(name, age), end=" ")
#     print("좋아하는 과목 : {} {} {} {} {}".format(subject1, subject2, subject3, subject4, subject5))
#     print()


def profile(name, age, *subject):
    print("이름 : {0},  나이 : {1},".format(name, age), end=" ")
    print("좋아하는 과목 : ", end=" ")
    for sub in subject:
        print(sub, end=" ")
    print()


profile("이재훈", 13, "수학", "영어", "과학", "국어", "도덕")
profile("삼재훈", 13, "수학", "영어")
profile("김개똥", 13, "수학", "영어", "국어", "미술", "체육", "음악")
