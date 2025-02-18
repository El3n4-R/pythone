class Message:
    def __init__(self, sender, recipient):
       
        self.sender = sender      # Mittente del messaggio
        self.recipient = recipient # Destinatario del messaggio
        self.text = ''            # Testo del messaggio (inizialmente vuoto)

       
        
    def set_text(self, text):
        """
        Imposta il testo del messaggio.
        
        :param text: Il contenuto del messaggio.
        """
        self.text = text
    
    def get_text(self):
        """
        Restituisce il testo del messaggio.
        
        :return: Il testo del messaggio.
        """
        return self.text
    
    def display(self):
        """
        Mostra le informazioni del messaggio.
        """
        print(f"Mittente: {self.sender}")
        print(f"Destinatario: {self.recipient}")
        print(f"Testo del messaggio: {self.text}")

    def append(self, line):
        """
        Aggiunge una riga in fondo al testo del messaggio.
        
        :param line: La riga da aggiungere al messaggio.
        """
        self.text += "\n" + line  # Aggiunge una nuova riga con il testo fornito
    
    def display(self):
        """
        Mostra le informazioni del messaggio.
        """
        print(f"Mittente: {self.sender}")
        print(f"Destinatario: {self.recipient}")
        print(f"Testo del messaggio:\n{self.text}")

# Creazione di un oggetto Message
msg = Message("massimo@hotmail.com", "rscura2@gmail.com")

# Impostazione del testo del messaggio
msg.set_text("Ciao Massimo, come stai?")

# Visualizzazione del messaggio
msg.display()

        # Aggiunta di righe successive
msg.append("Spero che tu stia passando una buona giornata.")
msg.append("Ci sentiamo presto!")

# Visualizzazione del messaggio
msg.display()
