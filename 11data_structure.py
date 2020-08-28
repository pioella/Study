menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


# --------------------------
from random import *
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = range(1, 21) # 1부터 21 바로 앞 숫자까지 range 클래스를 생성
print(type(lst))
lst = list(lst)
shuffle(lst)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 :", lst[0])
print("커피 당첨자 :", lst[1:4])
print("축하합니다.")

