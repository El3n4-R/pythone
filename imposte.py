imposta = 0
reddito=int(input("Qual è il tuo reddito? "))

# Calcolo per il primo scaglione (fino a 28.000 euro)
if reddito <= 28000 :
    imposta = reddito * 0.23

# Calcolo per il secondo scaglione (da 28000 a 50.000 euro)
elif reddito <= 50000 :
    imposta = 28000 * 0.23 + (reddito - 28000) * 0.35
    
 # Calcolo per il terzo scaglione (oltre 50000)
elif reddito > 50000 :
    imposta = 28000 * 0.23 + (50000 - 28000) * 0.35 + (reddito - 50000) * 0.43

print(imposta)
