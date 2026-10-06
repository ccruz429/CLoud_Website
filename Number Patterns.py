a = 1
b = 2
c = 3
option = int(input("Escoge una opcion: "))
n = int(input("Ingrese un numero: "))

if option == 1:
    for i in range(1, n + 1):
        print(" ".join(str(x) for x in
    range(1, i + 1)))
elif option == 2:
        for i in range(n, 0, -1):
            print(" ".join(str(x) for x in
        range(1, i + 1)))
elif option == 3:
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            numbers = " ".join(str(x) for x
        in range(1, i + 1))
            print(spaces + numbers)
else:
    print("Opción inválida. Por favor, elige 1, 2 o 3.")