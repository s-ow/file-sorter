# FileSorter - Organisateur de fichiers par extension

FileSorter est un outil simple en Python conçu pour vous aider à organiser vos fichiers en fonction de leurs extensions dans des dossiers spécifiques. Il peut trier les fichiers en catégories prédéfinies et créer des sous-dossiers pour chaque extension, vous permettant de maintenir un espace de stockage bien organisé.

## Fonctionnalités

- Triez vos fichiers en catégories prédéfinies, telles que "Images", "Documents", "Musique", "Vidéos", etc.
- Créez des sous-dossiers pour chaque extension de fichier.
- Gérez les fichiers inconnus en les plaçant dans un dossier "Autres".
- Personnalisez les catégories et les extensions selon vos besoins.

## Configuration

1. Assurez-vous d'avoir Python installé sur votre système.

2. Clonez ce référentiel ou téléchargez le fichier source.

3. Personnalisez (si besoin) les catégories et extensions dans le code source (voir `categories`, *ligne 24* dans le code).

4. Exécutez le script Python pour trier vos fichiers. Par défaut, les fichiers seront triés dans le dossier de téléchargements de l'utilisateur.

## Utilisation

1. Exécutez le script Python `main.py`.

2. Les fichiers seront triés dans des dossiers spécifiques en fonction de leurs extensions.

3. Les fichiers dont l'extension est inconnue seront placés dans un dossier "Autres" et dans des sous-dossiers portant le nom de leur extension.

## Exemple
Avant le tri :
```typescript
C:/Users/VotreNom/Downloads/
    ├── image1.jpg
    ├── document1.pdf
    ├── music.mp3
    ├── video.mp4
    ├── presentation.pptx
    ├── unknown.xyz
```
Après le tri :
```typescript
C:/Users/VotreNom/Downloads/
    ├── Images/
    │   ├── jpg/
    │   │   └── image1.jpg
    ├── Documents/
    │   ├── pdf/
    │   │   └── document1.pdf
    │   ├── pptx/
    │   │   └── presentation.pptx
    ├── Musique/
    │   ├── mp3/
    │       └── music.mp3
    ├── Vidéos/
    │   ├── mp4/
    │       └── video.mp4
    ├── Autres/
    │   ├── xyz/
    │       └── unknown.xyz

```