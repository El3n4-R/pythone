Y = ("pet")
N = ("item")
Aliquota = 0.2
lista_produtos = (Y, N)

vendas = input("Digita il prezzo di ogni prodotto seguito da Y per pet o N per oggetto: ")
Spesa_totale = float(input("Scrivi il totale del costo dei prodotti : " ))
Spesa_escluso_Y = float(input("Scrivi il totale del costo dei prodotti N : " ))
Vendas_Y = (vendas.count("Y"))
print(Vendas_Y)
Vendas_N = (vendas.count("N"))
print(Vendas_N)

if Vendas_Y >= 1 and Vendas_N >= 5 :
Sconto = float(Spesa_escluso_Y * Aliquota)
print(Sconto)
Pagamento_tot = (Spesa_totale - Sconto)
print(Pagamento_tot)
