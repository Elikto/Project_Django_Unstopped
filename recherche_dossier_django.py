import subprocess

subprocess.run('color 3', shell=True)
subprocess.run('cls', shell=True)
# Commande PowerShell pour rechercher le sous-dossier 'merchex'
powershell_command = r'''
$subfolders = Get-ChildItem -Directory -Path 'C:\Users\Formation\' -Recurse
foreach ($subfolder in $subfolders) {
    $merchexFolder = Get-ChildItem -Path $subfolder.FullName -Directory -Filter 'merchex' -ErrorAction SilentlyContinue
    if ($merchexFolder -ne $null) {
        $subfolder.FullName
    }
}
'''

# Exécution de la commande PowerShell
result = subprocess.run(['powershell', '-Command', powershell_command], capture_output=True, text=True)

# Récupération du résultat dans une variable Python
merchex_folders = result.stdout.strip().split('\n')

# Affichage des sous-dossiers contenant 'merchex'
for folder in merchex_folders:
    print("Le dossier 'merchex' a été trouvé dans le sous-dossier", folder)
