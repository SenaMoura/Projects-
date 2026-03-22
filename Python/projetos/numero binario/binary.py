def decimal_para_binario(n):
    if n == 0:
        return "0"   
    
    binario = ""
    while n > 0:
        resto = n % 2
        binario = str(resto) + binario
        n = n // 2
    return binario

num = int(input("Escreva um número decimal para converter em número binário: "))
print(f"O binário de {num} é {decimal_para_binario(num)}")

