# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# значение 0 - истина, значение 1 - ложь

for X in range(0, 2):
    for Y in range(0, 2):
        for Z in range(0, 2):
            if (not (X or Y or Z) == (not X)) and (not (X or Y or Z) == (not Y)) and (not (X or Y or Z) == (not Z)):
                print(f'X={X}, Y={Y}, Z={Z} -> Утверждение истинно')
            else:
                print(f'X={X}, Y={Y}, Z={Z} -> Утверждение ложно')
