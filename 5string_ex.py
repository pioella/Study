sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬어요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)
sentence4 = '''
안녕하세요
반갑습니다'''
print(sentence4)

"""
안녕하세요
"""

jumin = "990120-1234567"

print("성별 : " + jumin[7])  # index는 0부터 시작
print("생년 : " + jumin[0:2])  # 0번째부터 2번째 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6])

print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])  # 맨뒤에서 7번째부터 끝까지

print("--------------------------------------------------")
print("-" * 50)
