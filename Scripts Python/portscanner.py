import socket

# Input dell'utente per l'IP target della scansione
target = input("Inserisci l'IP per la scansione: ")

# Input dell'utente per il range delle porte da scansionare
portrange = input("Inserisci il range delle porte per la scansione: ")

# Estrai la porta inferiore e superiore dal range specificato dall'utente
lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

# Stampa delle informazioni sulla scansione
print('Scansione', target, 'dalla porta', lowport, 'alla porta', highport)

# Ciclo attraverso tutte le porte nel range specificato
for port in range(lowport, highport):
    # Creazione di un oggetto socket per la connessione
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Tentativo di connessione alla porta corrente dell'IP target
    status = s.connect_ex((target, port))
    
    # Verifica se la connessione è riuscita (status 0) e stampa il servizio associato alla porta
    if status == 0:
        service = socket.getservbyport(port)
        print('Porta', port, 'aperta - Servizio:', service)
    
    # Chiusura della connessione
    s.close()
