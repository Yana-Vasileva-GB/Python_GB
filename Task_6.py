# Task 6.
# Проверить ложность утверждения
# (x ≡ z) V (x → (y Λ z))

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not ((x == z) or (x <= y and z)):
                print(x, y, z)
