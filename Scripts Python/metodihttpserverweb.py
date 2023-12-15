import requests

def enumerare_metodi_http(target_url):
    # Lista dei metodi HTTP da testare
    metodi_http = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "TRACE", "PATCH"]

    for metodo in metodi_http:
        try:
            # Costruisci l'URL con il metodo corrente e la porta 80 se manca il prefisso "http://"
            url = f"{target_url}:{80 if 'http://' in target_url else ''}"
            
            # Effettua la richiesta HTTP con il metodo corrente
            risposta = requests.request(metodo, url)
            
            # Verifica se la risposta ha uno status code inferiore a 400 (successo)
            if risposta.status_code < 400:
                print(f"Il metodo {metodo} e' abilitato")
        except requests.exceptions.RequestException as e:
            # Gestisci eventuali eccezioni durante il test del metodo corrente
            print(f"Si e' verificato un errore durante il test del metodo {metodo}: {e}")

# Input dell'utente per l'URL target
target_url = input("Inserisci l'URL target: ")
enumerare_metodi_http(target_url)

