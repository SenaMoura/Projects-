print("\n///////////////Calculadora////////////////")
print("\n opção 1 - Adição")
print("\n opção 2 - Subtração")
print("\n opção 3 - Divisão")
print("\n opção 4 - Multiplicação")
opcao_escolha = int(input("Escolha umas das opções:"))

if(opcao_escolha == 1):
    soma_uma = int(input("Escreva o primeiro número que você quer somar: "))
    soma_dois = int(input("Escreva o segundo número que você quer somar: "))
    
    resultado_soma = soma_uma + soma_dois
    resultado_soma = abs(resultado_soma)

    print(f"O resultado da sua soma é: {abs(resultado_soma)}")
elif(opcao_escolha == 2):
    subtracao_uma = int(input("Escreva o primeiro número que você quer subtrair: "))
    subtracao_dois = int(input("Escreva o segundo número que você quer subtrair: "))

    resultado_sub = subtracao_uma - subtracao_dois
    resultado_sub = abs(resultado_sub)

    print(f"O resultado da sua soma é: {abs(resultado_sub)}")
elif(opcao_escolha == 3):
    div_uma = float(input("Escreva o primeiro número que você quer dividir: "))
    div_dois = float(input("Escreva o segundo número que você quer dividir: "))

    resultado_div = div_uma / div_dois
    resultado_div = abs(resultado_div)

    print(f"O resultado da sua soma é: {abs(resultado_div)}")
elif(opcao_escolha == 4):
    multi_uma = float(input("Escreva o primeiro número que você quer multiplicar: "))
    multi_dois = float(input("Escreva o segundo número que você quer multiplicar: "))

    resultado_multi = multi_uma * multi_dois
    resultado_multi = abs(resultado_multi)

    print(f"O resultado da sua soma é: {abs(resultado_multi)}")

