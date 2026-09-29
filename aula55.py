"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num_inteiro = input("Digite um número inteiro: ")

# if not num_inteiro.isdigit():
#     print("Isso não é um número inteiro.")
# else:
#     num_inteiro = int(num_inteiro)
#     if num_inteiro % 2 == 0:
#         print(f"O número {num_inteiro} é par.")
#     else:
#         print(f"O número {num_inteiro} é ímpar.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input("Digite a hora(um número inteiro): ")

# if not hora.isdigit():
#     print("Isso não é um número inteiro.")
# else:
#     hora = int(hora)
#     if 0 <= hora <= 11:
#         print("Bom dia!")
#     elif 12 <= hora <= 17:
#         print("Boa tarde!")
#     elif 18 <= hora <= 23:
#         print("Boa noite!")
#     else:
#         print("Hora inválida.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome é curto.") 
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")