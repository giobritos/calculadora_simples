value1 = input("Primeiro valor:  ")
value2 = input("Segundo valor: ")
expMath = input(" - Adição\n - Subtração\n - Divisão\n - Multiplicação\n - Potenciação\n Selecione o tipo de operação: ")

if expMath == "Adição":
    result1 = float(value1) + float(value2)
    print(result1)

elif expMath == "Subtração":
    result2 = float(value1) - float(value2)
    print(result2)

elif expMath == "Divisão":
    result3 = float(value1) / float(value2)
    print(result3)

elif expMath == "Multiplicação":
    result4 = float(value1) * float(value2)
    print(result4)

elif expMath == "Potenciação":
    result5 = float(value1) ** float(value2)
    print(result5)

else:
    print("Operação inválida!")
