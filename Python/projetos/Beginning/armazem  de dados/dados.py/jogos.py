import time

while True:
    preco = float(input("Por favor escreva o valor do seu jogo aqui porfavor: "))
    desconto = int(input("Escreva o valor desejado do desconto que você pretende aplicar: "))

    if desconto <= 30:
        valor_final = preco * desconto / 100 
        print(f"Valor registrado! O seu produto ficou R${valor_final}!")
        time.sleep(3)
        print("Obrigado por utilizar a nossa loja!")
        break
    else:
         print("O valor do desconto deve ser até 30%, você está aplicando um valor muito alto, porfavor reescreva o valor: ")
        