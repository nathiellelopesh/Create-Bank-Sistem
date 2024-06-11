menu = """
O que deseja fazer?

  [1] - Depositar
  [2] - Sacar
  [3] - Extrato
  [4] - Sair

"""

saldo = 0
qtd_saque = 0
qtd_deposito = 0

while True:
  opcao = int(input(menu))

  if opcao == 1:
    valor_deposito = float(input("Qual o valor a ser depositado?"))
    if valor_deposito <= 0:
      print("Informe um valor positivo")
    else:
      saldo += valor_deposito
      qtd_deposito += 1
      print(f"{valor_deposito} foi depositado com sucesso!")

  if opcao == 2:
    valor_saque = float(input("Qual o valor de saque?"))
    
    if qtd_saque > 3 or valor_saque > 500:
      print("Limite de 3 saques por dia de 500 reais")
      
    if valor_saque > saldo:
      print("Valor insuficiente em conta")
    elif valor_saque <= 0:
      print("Informe um valor positivo")
    else:
      saldo -= valor_saque
      qtd_saque += 1
      print(f"{valor_saque} foi sacado com sucesso!")
      
  if opcao == 3:
    if saldo <= 0:
      print("Não foi realizado nenhuma movimentação bancária")
    else:
      print(f"""
        Saldo: R$ {saldo}
        Quantidade de saque: {qtd_saque}
        Quantidade de deposito: {qtd_deposito}
        """)

  if opcao == 4:
    break