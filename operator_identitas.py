# Operator identitas
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True (b menunjuk objek yang sama dengan a)
print(a is c) # False (c objek berbeda walau isinya sama)
print(a == c) # True (nilai isinya sama)
