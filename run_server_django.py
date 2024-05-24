import subprocess

def run_server():
    while True:
        try:        
            subprocess.run('color 3', shell=True)
            subprocess.run('cls', shell=True)
            command = 'cmd /c "cd C:\\Users\\Formation\\Documents\\algo\\django-web-app\\merchex && python manage.py runserver"'
            print("Serveur Django en cours d'exécution...")
            process = subprocess.Popen(command, shell=True)
            process.wait()  # Attend que le processus se termine
            print("Le serveur Django s'est arrêté.")
            user_input = input("Entrez '1' pour redémarrer ou 'exit' pour quitter: ")
            if user_input.lower() == 'exit':
                break  # Quitte la boucle si l'utilisateur choisit de quitter
        except KeyboardInterrupt:
            pass  # Ignore l'erreur KeyboardInterrupt (CTRL + C)
        except Exception as e:
            print(f"Erreur: {e}")

if __name__ == "__main__":
    run_server()

