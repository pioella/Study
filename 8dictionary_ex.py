cabinet = {3: "유재석", 100: "조세호"}
print(cabinet)
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A3": "유재석", "C100": "하하"}
print(cabinet["A3"])
print(cabinet["C100"])

print(cabinet)
cabinet["A3"] = "김종국"
cabinet["B20"] = "조세호"
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())
print(cabinet)

del cabinet["A3"]
print(cabinet)

cabinet.clear()
print(cabinet)


