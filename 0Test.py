import copy
from tkinter import *

# root = Tk()
# root.title("Pioella")
# root.geometry("640x480+300+100")
# root.resizable(False, False)
# root.mainloop()


# list1 = ["이재훈", "이대희"]
# list2 = list1
#
# list1.append("박선영")
# print(list1)
# print(list2)
#
# r1 = ['hi', [180, 25], ('hello')]
# r2 = list(r1)
# print(type(r1))
# print(r1 == r2)
# print(r1 is r2)
# r2.append("bye")
# print(r1)
# print(r2)
# print(r1[0] is r2[0])
# r2 = copy.deepcopy(r1)
# print(r1 is r2)
# print(r1[0] == r2[0])
# print(r1[0] is r2[0])

# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(lst[9:19])


def calculate_standard_weight(height, gender):
    if gender == "남자":
        standard_weight = height * height * 22
    else:
        standard_weight = height * height * 21

    # standard_weight = int(standard_weight * 100 + 0.5) / 100
    standard_weight = round(standard_weight, 2)

    print(standard_weight)


calculate_standard_weight(1.75, "남자")
calculate_standard_weight(1.75, "여자")

