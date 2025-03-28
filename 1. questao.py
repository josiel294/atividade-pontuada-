"""
Informe o número da turma: 
Turma - 

Nome completo dos componentes.
1 - Josiel Santos Cezario
2 - Rui Lopes Ferreira

"""


import os

# Limpa o terminal.
os.system("cls || clear") 

pedidos = []
valor_total = 0




print(""""
================= MENU =============
Código  \tPrato            \t\tValor                     
1  \t\tPicanha         \t\t25,00                      
2  \t\tLasanha          \t\t20,00                      
3  \t\tStrogonoff      \t\t18,00                      
4  \t\tbife acebolado  \t\t15,00                  
5  \t\tPão com ovo     \t\t5,00                      
6  \t\tPão com salsicha     \t\t8,50                      
7  \t\tCuscuz com calabresa   \t\t12,00                      
""")


while True:
    pratos = int(input("Dígite o prato desejado (1-7): "))
    if pratos == 1:
        prato = "Picanha"
        pedidos.append("Prato 1 - valor R$25,00")
        valor_total += 25.00
        print("Prato escolhido: Picanha")
    elif pratos == 2:
        prato = "Lasanha"
        pedidos.append("Prato 2 - valor R$20,00")
        valor_total += 20.00
        print("Prato escolhido: Lasanha")
    elif pratos == 3:
        prato = "Strogonoff"
        pedidos.append("Prato 3 - valor R$18,00")
        valor_total += 18.00
        print("Prato escolhido: Strogonoff")
    elif pratos == 4:
        prato = "Bife acebolado"
        pedidos.append("Prato 4 - valor R$15,00")
        valor_total += 15.00
        print("Prato escolhido: Bife acebolado")
    elif pratos == 5:
        prato = "Pão com ovo"
        pedidos.append("Prato 5 - valor R$5,00")
        valor_total += 5.00
        print("Prato escolhido: Pão com ovo")
    elif pratos == 6:
        prato = "Pão com salsicha"
        pedidos.append("Prato 6 - valor R$8,50")
        valor_total += 8.50
        print("Prato escolhido: Pão com salsicha ")
    elif pratos == 7:
        prato = "Cuscuz com calabresa"
        pedidos.append("Prato 7 - valor R$12,00")
        valor_total += 12.00
        print("Prato escolhido: Cuscuz com calabresa")
        break
    else:
        print("opção invalida, tente novamente")
        continue
    
    continuar = input("\nDeseja escolher outro prato? (Sim:1 e Não:0 ):")
    if continuar !='1':
        break

print(""""
================= FORMA DE PAGAMENTO =============
Código  \tPrato                      
1  \t\tÁ vista ou pix                   
2  \t\tÁ cartão de crédito                            
""")




pagamento = int(input("forma de pagamento: "))
match pagamento:
    case 1:
        desconto = (valor_total * 0.10)
        valor_com_desconto = valor_total - desconto
        print(f"\nForma de pagamento: Á vista ")  
        print(f"\nValor do desconto R$:{desconto} ")  
        print(f"\nValor do produto R$:{valor_total} ")  
        print(f"\nValor do produto com desconto R$: {valor_com_desconto} ") 
    case 2:
        parcelas = int(input("Quantas parcelas você deseja (1-4): "))
        acrescimo = (valor_total * 0.10)
        if parcelas >= 1 and parcelas <= 4:
            valor_da_parcela = (valor_total / parcelas) + acrescimo
            print(f"\nValor do produto: R$ {valor_total}")
            print(f"Forma de pagamento: à cartão de crédito")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R$ {valor_da_parcela:.2f}")
            print(f"Total à prazo: R$ {valor_da_parcela:.2f}")
        else:
            print("Opção inválida")

    case _:
        print("Opção invalida")