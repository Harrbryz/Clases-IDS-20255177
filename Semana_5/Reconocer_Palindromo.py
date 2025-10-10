reconocer_palindromo = input("Ingrese una palabra para ver si es un palindromo: ").lower()
inverso = reconocer_palindromo[::-1]
if reconocer_palindromo == inverso:
    print(f"{reconocer_palindromo.upper}Es un palindromo")
else:
    print("No es un palindromo")