# Générer un exécutable Windows

Ce dépôt peut être empaqueté en `.exe` pour lancer le serveur FastAPI sans
installer Python sur la machine cible. Le binaire démarre Uvicorn et sert
l'interface web comme d'habitude.

## Pré-requis

- Windows 10/11 avec Python 3.11+ installé
- Pip disponible dans le `PATH`
- Accès à internet pour installer les dépendances

## Étapes

1. Cloner le projet sur la machine Windows.
2. Installer les dépendances d'exécution et de build :

   ```powershell
   pip install -r requirements.txt -r requirements-build.txt
   ```

3. Générer l'exécutable :

   ```powershell
   python .\scripts\build_windows_exe.py
   ```

   Le dossier `dist/IEChargeDashboard/` contient alors `IEChargeDashboard.exe`
   prêt à l'emploi. Les répertoires `assets`, `static` et `templates` sont
   inclus automatiquement.

4. Lancer l'application depuis n'importe où :

   ```powershell
   dist\IEChargeDashboard\IEChargeDashboard.exe
   ```

   Par défaut le serveur démarre sur `http://127.0.0.1:8000`.

## Remarques

- L'exécutable utilise le mode `onedir` pour garder les ressources accessibles
  sans extraction lente en mémoire.
- Les chemins des templates et fichiers statiques sont résolus à l'exécution
  (compatible PyInstaller) ; il n'est pas nécessaire de placer l'exécutable dans
  le répertoire du code source.
- Si le port 8000 est occupé, vous pouvez définir la variable d'environnement
  `UVICORN_PORT` puis exécuter le binaire, ou créer un raccourci avec un autre
  port et ajouter `--port 9000` à la ligne de commande.
