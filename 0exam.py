from random import randint

customers = range(1, 51)
board_count = 0
for customer in customers:
    customer_time = randint(5, 51)
    board = " "
    if customer_time <= 15:
        board = "O"
        board_count += 1

    print("[{0}]{1}번째 손님 (소용시간 : {2}분)".format(board, customer, customer_time))
print("총 탑승 승객 : {}분".format(board_count))




