import os
import subprocess

def find_folder():
    subprocess.run('color 3', shell=True)
    subprocess.run('cls', shell=True)
    
    # Demander le nom du projet Django à l'utilisateur
    my_folder = input('Entrez le nom de votre projet Django, par défaut "merchex" : ') or 'merchex'
    
    # Commande PowerShell pour rechercher le sous-dossier avec le nom spécifié
    powershell_command = f'''
    $subfolders = Get-ChildItem -Directory -Path 'C:\\Users' -Recurse
    foreach ($subfolder in $subfolders) {{
        $folder = Get-ChildItem -Path $subfolder.FullName -Directory -Filter '{my_folder}' -ErrorAction SilentlyContinue
        if ($folder -ne $null) {{
            Write-Output $folder.FullName
        }}
    }}
    '''
    
    # Exécution de la commande PowerShell
    result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True)
    
    # Récupération du résultat dans une variable Python
    folder_paths = result.stdout.strip().split('\n')
    
    if folder_paths and folder_paths[0]:
        for index, path in enumerate(folder_paths, start=1):
            print(f"{index}: Le dossier '{my_folder}' a été trouvé dans le sous-dossier {path}")
        
        while True:
            user_input = input("Entrez le numéro du dossier que vous souhaitez utiliser ou 'exit' pour quitter: ")
            if user_input.lower() == 'exit':
                return
            elif user_input.isdigit() and 1 <= int(user_input) <= len(folder_paths):
                chosen_folder_path = folder_paths[int(user_input) - 1].replace('\\', '\\\\')
                break
            else:
                print("Entrée invalide. Veuillez entrer un numéro de dossier valide ou 'exit' pour quitter.")
        
        # Créer un dossier 'DjangoUnstopped' dans le répertoire Documents de l'utilisateur
        user_documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
        django_unstopped_path = os.path.join(user_documents_folder, "DjangoUnstopped")
        os.makedirs(django_unstopped_path, exist_ok=True)
        
        # Créer le fichier 'runserver.py' dans le dossier 'DjangoUnstopped'
        run_server_script = f"""
import subprocess

def run_server():
    while True:
        try:
            subprocess.run('color 3', shell=True)
            subprocess.run('cls', shell=True)
            command = r'cmd /c "cd {chosen_folder_path} && python manage.py runserver"'
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
            print(f"Erreur: {{e}}")

if __name__ == "__main__":
    run_server()
"""

        # Créer le fichier 'makemigration_migrate.py' dans le dossier 'DjangoUnstopped'
        makemigration_migrate_script = f"""
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
            command = r'cmd /k "cd {chosen_folder_path} && python manage.py makemigrations && python manage.py migrate"'
            print("Exécution des migrations Django...")
            # Exécution de la commande dans un nouveau processus
            subprocess.run(command, shell=True)
        else:
            print("Entrée invalide. Veuillez entrer '1' pour exécuter la commande ou 'exit' pour quitter.")

if __name__ == "__main__":
    run_command()
"""

        run_server_file_path = os.path.join(django_unstopped_path, "runserver.py")
        with open(run_server_file_path, "w", encoding="utf-8") as file:
            file.write(run_server_script.strip())

        makemigration_migrate_file_path = os.path.join(django_unstopped_path, "makemigration_migrate.py")
        with open(makemigration_migrate_file_path, "w", encoding="utf-8") as file:
            file.write(makemigration_migrate_script.strip())

        print(f"Les fichiers 'runserver.py' et 'makemigration_migrate.py' ont été créés dans {django_unstopped_path}")
    else:
        print(f"Le dossier '{my_folder}' n'a pas été trouvé.")
    
    return folder_paths

if __name__ == "__main__":
    found_paths = find_folder()
