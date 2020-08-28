python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))

print(python.find("Java"))
# print(python.index("java"))
print("hi")

print(python.count("n"))

print("a" + "b")
print("a", "b")

print("나는 20살입니다.")
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s살입니다." % 20)
print("Apple은 %s로 시작해요." % "A")

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다." . format(20))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age=20))

# 파이썬 버전 3.6 이상부터 사용가능
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
print("백문이 불여일견\n백견이 불여일타")
# 저는 "이대희"입니다.
print('저는 "이대희"입니다.')
print("저는 \"이대희\"입니다.")

# 문장 내에서 \
print("c:\\user\\dog77\\")

# \r 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b 백스페이스
print("Redd\bApple")
# \t tap
print("Red\n\tApple")

#--------------------------
uri = "http://naver.com"
uri = uri.replace("http://", "")
print(uri)
uri = uri[:uri.index(".")]
print(uri)
uri = uri[:3] + str(len(uri)) + str(uri.count("e")) + "!"
print(uri)

