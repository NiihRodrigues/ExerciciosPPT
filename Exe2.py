valor_compra = float(input("Informe o valor da compra: R$"))
parcelas = int(input("Informe quantas parcelas deseja: "))

valor_parcela = valor_compra / parcelas

print(f"O valor da compra foi de R${valor_compra} ,"
      f"o número de parcelas informado foi {parcelas} "
      f"e o valor da parcela é R$%.2f." % valor_parcela)
