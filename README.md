# Project_Django_Unstopped

Django Unstopped est un programme qui permet d'avoir 2 fenêtres de terminal qui restent toujours ouverte, une qui lance le serveur et une autre qui fait les commandes makemigration et migrate

La première fênetre qui lance le serveur Django ne s'arrete pas, lors de l'appui sur CTRL + C le serveur redemarre, pour fermer le serveur il suffit de fermer la fenêtre.

La seconde fênetre lance les commandes makemigration et migrate lors de l'appui sur la touche ENTREE, le programme redemande en boucle ce que vous voulez faire, ENTREE pour lancer les commandes et "exit" pour quitter.


Procédure d'installation : 
Lancer le fichier Setup_DjangoUnstopped.py

Ecrire le nom du dossier Django (par exemple 'merchex' ou 'mysite')

Selectionner le dossier voulu parmis la liste
    Vous devez selectionner le dossier parent pas le sous dossier qui comporte le même nom
    Par exemple dans l'image ci-dessous 
    
    ![Choix dossier Django](choix_dossier.png)

    il faut sélectionner
    " 1: Le dossier 'merchex' a été trouvé dans le sous-dossier C:\Users\Formation\Documents\algo\django-web-app\merchex "

Lancer le programme à partir du raccourci crée sur le bureau 

Le programme 'DjangoUnstopped.bat se trouve ' dans le dossier "DjangoUnstopped" dans le dossier "Mes Documents"



le fichier Setup_DjangoUnstopped.py va trouver les dossiers Django portant le nom voulu (par exemple 'merchex' ou 'mysite'), il créer ensuite un dossier "DjangoUnstopped" dans le dossier "Mes Documents" ou se trouveront les fichier runserver.py et makemigration.py


