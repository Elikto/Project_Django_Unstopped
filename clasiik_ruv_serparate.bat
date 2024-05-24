@echo off


rem Lancer le serveur Django dans une nouvelle fenêtre de commande
start cmd /k "python run_server_django.py"

rem Attendre un court instant pour que la première fenêtre se lance complètement
timeout /t 2 /nobreak >nul

rem Exécuter les migrations Django dans une nouvelle fenêtre de commande
start cmd /k "python migrate_django.py"

