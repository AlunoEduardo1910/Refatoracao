try:
    numero_1 = float(input("Digite um número:"))
    numero_2 = float(input("Digite outro número:"))

    soma = numero_1 + numero_2
    diferenca = numero_1 - numero_2
    produto = numero_1 * numero_2
    divisao = numero_1 / numero_2

    print(f"A soma dos seguintes números é {soma}\nA diferença é {diferenca} \nO produto é {produto}\nA divisao é {divisao}")

except:
    print("Por gentileza, digite um número")