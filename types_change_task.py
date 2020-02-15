print(float('1'))
try:
    print(int("2.5"))
except ValueError:
    print("Ошибка") 
print(bool(1))
print(bool(" "))
print(bool(0))