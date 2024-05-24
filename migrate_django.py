import subprocess

def run_command():
    while True:
        subprocess.run('color 2', shell=True)
        user_input = input('Entrez 1 pour exécuter "python manage.py makemigrations && python manage.py migrate" ou "exit" pour quitter: ')
        if user_input.lower() == 'exit':
            break
        elif user_input == '1':
            # Construction de la commande à exécuter
            subprocess.run('cls', shell=True)
            command = 'cmd /c "cd C:\\Users\\Formation\\Documents\\algo\\django-web-app\\merchex && python manage.py makemigrations && python manage.py migrate"'
            print("Exécution des migrations Django...")
            # Exécution de la commande dans un nouveau processus
            subprocess.run(command, shell=True)
        else:
            print("Entrée invalide. Veuillez entrer '1' pour exécuter la commande ou 'exit' pour quitter.")

if __name__ == "__main__":
    run_command()
