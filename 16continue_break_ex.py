absent = [5, 7]
no_book = [6]

for student in range(1, 11):
    # if student == 5:
    if student in absent:
        continue
    elif student in no_book:
        print("{}번, 앞으로 나와".format(student))
        break
    print("{}번, 출석~".format(student))

print()

n = 0
while n <= 100:
    print(n)
    n += 1
    if n > 50:
        break

for n in range(1, 51):
    if n % 2 == 0:
        continue
    print(n)

