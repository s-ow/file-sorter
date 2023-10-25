""" 
                                                                    MAQUETTE DU PROGRAMME
regarder l'extension
-> dossier ?
    -> oui
        -> pas touche
    -> non
        -> regarder l'extension
            -> normale
                -> check si dossier
                    -> dossier existe
                        -> ranger dans dossier
                    -> dossier existe pas
                        -> créer dossier
                            -> ranger dans dossier
            -> anormale
                -> check si dossier autres
                    -> dossier existe
                        -> check si dossier extension
                            -> dossier existe
                                -> ranger dans dossier
                            -> dossier existe pas
                                -> créer dossier
                                    -> ranger dans dossier
                    -> dossier existe pas
                        -> créer dossier
                            -> créer dossier extension
                                -> ranger dans dossier
"""

import os
import shutil

# extensions triées par catégories (merci ChatGPT je ne connaissais pas tout ça)
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif"],
    "Documents": [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".html", ".css", ".js", ".txt", ".rtf", ".csv"],
    "Musique": [".mp3", ".wav", ".flac", ".aac"],
    "Vidéos": [".mp4", ".avi", ".mkv", ".wmv", ".mov", ".flv"],
    "Archives": [".rar", ".zip", ".gz", ".7z", ".tar"],
    "Exécutables": [".exe", ".msi"],
    "Scripts": [".py", ".sh", ".bat"],
    "Configuration": [".ini", ".cfg", ".json"],
    "Images_ISO": [".iso", ".img"],
    "Code Source": [".c", ".cpp", ".java", ".cs", ".php", ".js", ".html", ".css", ".py"],
    "Feuilles de Calcul": [".xls", ".xlsx", ".ods", ".csv"],
    "Présentations": [".ppt", ".pptx", ".key"],
    "Livres Électroniques": [".epub", ".mobi", ".azw"],
    "Fichiers de Données": [".json", ".xml", ".yaml", ".sql"],
    "Fichiers de Configuration": [".ini", ".cfg"],
    "Fichiers de Texte": [".txt", ".md", ".log"],
    "Fichiers de Licences": [".lic", ".license"],
    "Fichiers de Code Source": [".c", ".cpp", ".h", ".hpp", ".java", ".cs", ".php", ".js", ".html", ".css", ".py"],
    "Fichiers de Base de Données": [".db", ".sqlite", ".sql", ".mdb", ".accdb"],
    "Fichiers d'Images Matricielles": [".bmp", ".tiff", ".pcx", ".pict"],
    "Fichiers d'Images Vectorielles": [".svg", ".ai", ".eps", ".pdf"],
    "Fichiers Audio Non-Compressés": [".wav", ".aiff", ".pcm"],
    "Fichiers Audio Compressés": [".mp3", ".ogg", ".wma"],
    "Fichiers Vidéo Haute Qualité": [".mkv", ".webm", ".m2ts"],
    "Fichiers Vidéo DVD": [".vob", ".ifo"],
    "Fichiers Vidéo Blu-ray": [".m2ts", ".ssif"],
    "Fichiers de Sous-Titres": [".srt", ".sub", ".ass"],
    "Fichiers de Jeux": [".sav", ".lvl", ".map", ".cfg"],
    "Fichiers de Projets": [".proj", ".sln", ".vcproj", ".xcodeproj"],
    "Fichiers de Virtualisation": [".vdi", ".vmdk", ".ova", ".qcow2"],
    "Fichiers de Modèles 3D": [".obj", ".stl", ".gltf", ".dae"],
    "Fichiers de Police": [".ttf", ".otf"],
    "Fichiers de CAD": [".dwg", ".dxf", ".igs"],
    "Fichiers de Torrent": [".torrent"],
    "Fichiers de Journal": [".log", ".logx", ".log1", ".log2"],
    "Fichiers de Feuille de Style": [".css", ".scss", ".less"],
    "Fichiers de Configuration Web": [".htaccess", ".webconfig"],
    "Fichiers de Paramètres": [".settings", ".config", ".prefs"],
    "Fichiers de Préprocesseur": [".inc", ".m4", ".asm", ".s"],
    "Fichiers de Présentations Markdown": [".md", ".markdown"],
    "Fichiers de Dictionnaires": [".dic", ".dict"],
    "Fichiers de Cryptographie": [".pem", ".cer", ".crt", ".key"],
    "Fichiers de Virtualenv Python": [".venv"],
    "Fichiers de Gestion de Version": [".gitignore", ".gitattributes"],
    "Fichiers de Docker": [".dockerfile"],
    "Fichiers de Config Ansible": [".yml", ".yaml"],
    "Fichiers de Texte Ascii-Art": [".asc", ".nfo", ".txt"],
}

utilisateur = os.getlogin()
dossier_downloads = f"C:/Users/{utilisateur}/Downloads"

fichiers = os.listdir(dossier_downloads)

for fichier in fichiers:
    chemin = dossier_downloads + "/" + fichier

    if os.path.isdir(chemin):
        pass
    else:
        extension = os.path.splitext(fichier)[1].lower()
        extension_sans_point = extension[1:]

        categorie = None
        for nom_categorie, extensions_categorie in categories.items():
            if extension in extensions_categorie:
                categorie = nom_categorie
                break

        if categorie:
            dossier_destination = os.path.join(dossier_downloads, categorie, extension_sans_point)

            if not os.path.exists(dossier_destination):
                os.makedirs(dossier_destination)

            source = chemin
            destination = os.path.join(dossier_destination, fichier)

            shutil.move(source, destination)
        else:
            dossier_destination = os.path.join(dossier_downloads, "Autres", extension_sans_point)

            if not os.path.exists(dossier_destination):
                os.makedirs(dossier_destination)

            source = chemin
            destination = os.path.join(dossier_destination, fichier)

            shutil.move(source, destination)
