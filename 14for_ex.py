# for waiting_no in [0, 1, 2, 3, 4]:
# for waiting_no in range(0, 5):
for waiting_no in range(2, 5):
    print("대기번호 : {}".format(waiting_no))

print()

family = ["이대희", "박선영", "이재훈"]
for name in family:
    print(name + "님, 안녕하세요.")


students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)


name_len = [len(name) for name in family]
print(name_len)

animals = ["cat", "dog", "horse", "mouse"]
print(animals)
animals = [animal.upper() for animal in animals]
print(animals)
