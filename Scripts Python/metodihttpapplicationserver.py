import http.client

# Richiesta all'utente dell'host (nome del dominio o indirizzo IP) del target
host = input("Inserire l'host/IP del target: ")

# Richiesta all'utente della porta del target
port = input("Inserire la porta del target: ")

try:	
    # Creazione di una connessione HTTP con l'host e la porta specificati
    connection = http.client.HTTPConnection(host, port)
    
    # Invio di una richiesta di tipo "OPTIONS" per ottenere i metodi HTTP abilitati
    connection.request("OPTIONS", "/")
    
    # Ottenimento della risposta dal server
    response = connection.getresponse()
    
    # Stampa dei metodi HTTP abilitati (basato sullo status code della risposta)
    print("I metodi abilitati sono: ", response.status)
    
    # Chiusura della connessione
    connection.close()
except ConnectionRefusedError:
    # Gestione dell'errore nel caso in cui la connessione al target fallisca
    print("CONNESSIONE FALLITA")
