ano = int(input("Digite o ano em que você nasceu?: "))
ano_atual = int(input("Digite o ano em que você está: "))

sua_idade = ano - ano_atual 
sua_idade = abs(sua_idade)

print(f"Você tem exatamente {abs(sua_idade)}")          


