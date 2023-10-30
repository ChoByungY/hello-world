# Dictionary

cabinet = {"A1": "유재석", "A3": "조세호"}

cabinet["C20"] = "황우연"

print(type(cabinet), cabinet)

print(cabinet["A1"])

print(cabinet.get("A3"))

print(cabinet.get("A7"))
print(cabinet.get("A7", "사용가능"))

del cabinet["A3"]

print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()


print(cabinet)