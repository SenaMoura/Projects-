
def binario_para_decimal(b):
    decimal = 0
    potencia = 0
    
    for digito in reversed(b):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1

    return decimal

while True:
    binario = input("Digite o número binário aqui porfavor: ")
    if len(binario) <= 8:
        print(f"O número binário {binario} foi convertido para {binario_para_decimal(binario)}")
        break
    else:
        print("Número binário muito longo, porfavor reescreva ele: ")



    
    

        

        


        



        
         

    









