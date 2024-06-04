import os
import subprocess
import winshell
from win32com.client import Dispatch

def find_folder():
    subprocess.run('color 3', shell=True)
    subprocess.run('cls', shell=True)
    
    my_folder = input('Entrez le nom de votre projet Django, par défaut "merchex" : ') or 'merchex'
    
    powershell_command = f'''
    $subfolders = Get-ChildItem -Directory -Path 'C:\\Users' -Recurse
    foreach ($subfolder in $subfolders) {{
        $folder = Get-ChildItem -Path $subfolder.FullName -Directory -Filter '{my_folder}' -ErrorAction SilentlyContinue
        if ($folder -ne $null) {{
            Write-Output $folder.FullName
        }}
    }}
    '''
    
    result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True)
    
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
        
        user_documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
        django_unstopped_path = os.path.join(user_documents_folder, "DjangoUnstopped")
        os.makedirs(django_unstopped_path, exist_ok=True)
        
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
            process.wait()
            print("Le serveur Django s'est arrêté.")
            user_input = input("Entrez '1' pour redémarrer ou 'exit' pour quitter: ")
            if user_input.lower() == 'exit':
                break
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"Erreur: {{e}}")

if __name__ == "__main__":
    run_server()
"""

        makemigration_migrate_script = f"""
import subprocess

def run_command():
    while True:
        subprocess.run('color 2', shell=True)
        user_input = input('Appuyez sur ENTREE pour exécuter "python manage.py makemigrations && python manage.py migrate" ou "exit" pour quitter: ')
        if user_input.lower() == 'exit':
            break
        elif not user_input:
            subprocess.run('cls', shell=True)
            command = r'cmd /c "cd {chosen_folder_path} && python manage.py makemigrations && python manage.py migrate"'
            print("Exécution des migrations Django...")
            subprocess.run(command, shell=True)
        else:
            print("Entrée invalide. Appuyez simplement sur ENTREE pour exécuter la commande ou 'exit' pour quitter.")

if __name__ == "__main__":
    run_command()
"""

        fichier_bat = f"""
@echo off
start cmd /k "python runserver.py"
timeout /t 2 /nobreak >nul
start cmd /k "python makemigration_migrate.py"
"""

        run_server_file_path = os.path.join(django_unstopped_path, "runserver.py")
        with open(run_server_file_path, "w", encoding="utf-8") as file:
            file.write(run_server_script.strip())

        makemigration_migrate_file_path = os.path.join(django_unstopped_path, "makemigration_migrate.py")
        with open(makemigration_migrate_file_path, "w", encoding="utf-8") as file:
            file.write(makemigration_migrate_script.strip())

        fichier_bat_path = os.path.join(django_unstopped_path, "DjangoUnstopped.bat")
        with open(fichier_bat_path, "w", encoding="utf-8") as file:
            file.write(fichier_bat.strip())

        # Utilisation de PyInstaller pour créer l'exécutable
        subprocess.run(['pyinstaller', '--onefile', fichier_bat_path])

        # Déplacement du fichier exécutable généré
        exe_file_path = os.path.join("dist", "DjangoUnstopped.exe")
        new_exe_file_path = os.path.join(django_unstopped_path, "DjangoUnstopped.exe")
        os.rename(exe_file_path, new_exe_file_path)

        desktop = winshell.desktop()
        shortcut_file_path = os.path.join(desktop, "DjangoUnstopped.lnk")
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_file_path)
        shortcut.Targetpath = new_exe_file_path
        shortcut.WorkingDirectory = os.path.dirname(new_exe_file_path)
        shortcut.save()

        print(f"Les fichiers 'runserver.py', 'makemigration_migrate.py' et 'DjangoUnstopped.bat' ont été créés dans {django_unstopped_path}")
        print(f"Le fichier exécutable 'DjangoUnstopped.exe' a été créé dans {django_unstopped_path}")
        print(f"Le raccourci vers 'DjangoUnstopped.exe' a été créé sur le bureau de l'utilisateur.")
    else:
        print(f"Le dossier '{my_folder}' n'a pas été trouvé.")
    
    return folder_paths

if __name__ == "__main__":
    found_paths = find_folder()
