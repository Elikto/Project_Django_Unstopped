# Project_Django_Unstopped

Django Unstopped est un programme qui permet d'avoir 2 fenêtres de terminal qui restent toujours ouverte, une qui lance le serveur Django et une autre qui fait les commandes makemigration et migrate

Plus besoin d'écrire manuellement les commandes 
```python manage.py runserver ```
et
```python manage.py makemigrations && python manage.py migrate```
DjangoUnstopped s'en charge


![terminal Server Django](picture/server.png)
La première fênetre qui lance le serveur Django ne s'arrete pas lors de l'appui sur CTRL + C !
Il redemarre, évitant de devoir le relancer manuellement à chaque fois
pour fermer le serveur il suffit de fermer la fenêtre.

![terminal commande makemigration et migrate](picture/migrate.png)
La seconde fênetre lance les commandes makemigration et migrate lors de l'appui sur la touche ENTREE
Le programme redemande en boucle ce que vous voulez faire en affichant les changements, 
ENTREE pour lancer les commandes et "exit" pour quitter.


Le fichier Setup_DjangoUnstopped.py va trouver les dossiers Django portant le nom voulu (par exemple 'merchex' ou 'mysite'), il créer ensuite un dossier "DjangoUnstopped" dans le dossier "Mes Documents" ou se trouveront les fichier runserver.py, makemigration.py et DjangoUnstopped.bat



# Procédure d'installation : 

Lancer le fichier Setup_DjangoUnstopped.py

Ecrire le nom du dossier Django (par exemple 'merchex' ou 'mysite')

Selectionner le dossier voulu parmis la liste :

Vous devez selectionner le dossier parent pas le sous dossier qui comporte le même nom

Par exemple dans l'image ci-dessous 

![Choix dossier Django](picture/choix_dossier.png)

il faut sélectionner la première ligne



# Utilisation

Lancer le programme à partir du raccourci 'DjangoUnstopped' crée sur le bureau 

ou à partir du programme 'DjangoUnstopped.bat' qui se trouve dans le dossier "DjangoUnstopped" dans le dossier "Mes Documents"

CTRl + C permet de relancer le serveur dans la première fenêtre

ENTREE lance les commandes makemigrations et migrate dans la deuxième fenêtre






