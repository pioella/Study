# print("이재훈", "13살")
# print("이재훈", "13살", sep=",  ")
# print("이재훈", "13살", sep=",  ")
# print("사과", "포도", "딸기", sep=", ", end=" 등은 과일입니다.")
# print()


# import sys
# print("Error", file=sys.stdout)
# print("Error", file=sys.stderr)

file = open("c://Download//test.txt", "w")
print("나는\t이재훈입니다.\n안녕하세요", file=file, flush=False)
file.close()

print("나는\t이재훈입니다.")


# score = {"수학":100, "영어":99, "코딩":95}
# for subject, scroe in score.items():
#     # print(subject, scroe)
#     print(subject.ljust(4), str(scroe).rjust(4), sep=":")
# print()

# for number in range(1,21):
#     print(("대기번호 : " + str(number).zfill(3)))

for money in range(1000, 20000, 1000):
    print("{:,}".format(money))

# answer = input("아무 값이나 입렵하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")
# print(type(answer))

