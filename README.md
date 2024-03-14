# Scraper Facebook avec Selenium

Ce projet permet de se connecter à Facebook, effectuer une recherche avec un hashtag spécifique et extraire le contenu des 10 premiers résultats de la recherche.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les dépendances suivantes :

- Python 3.x
- Google Chrome
- ChromeDriver compatible avec votre version de Google Chrome

## Installation

1. Clonez le dépôt sur votre machine locale :

```bash
git clone git@github.com:yasserxkamal/Fb__scraper.git
```

2. Accédez au répertoire du projet :

```bash
cd scraper-facebook
```

3. Créez un environnement virtuel Python et activez-le :

```bash
python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
```

4. Installez les dépendances requises :

```bash
pip install -r requirements.txt
```

5. Téléchargez la version de ChromeDriver correspondant à votre version de Google Chrome depuis le [site officiel](https://sites.google.com/a/chromium.org/chromedriver/downloads). Assurez-vous que le fichier exécutable `chromedriver` se trouve dans votre répertoire système `PATH`.

6. Créez un fichier `.env` à la racine du projet et remplissez-le avec les informations suivantes :

```
CHROME_DRIVER_PATH=/path/to/chromedriver
FB_EMAIL=votre_email@exemple.com
FB_PASSWORD=votre_mot_de_passe
HASHTAG=#Pizza
```

Remplacez les valeurs ci-dessus par vos propres informations :

- `CHROME_DRIVER_PATH` : Chemin d'accès complet vers l'exécutable `chromedriver` sur votre système.
- `FB_EMAIL` : Votre adresse e-mail Facebook.
- `FB_PASSWORD` : Votre mot de passe Facebook.
- `HASHTAG` : Le hashtag à rechercher sur Facebook.

## Utilisation

Une fois que tous les prérequis sont installés et que le fichier `.env` est configuré, vous pouvez exécuter le script avec la commande suivante :

```bash
python scraper.py
```

Le script se connectera à Facebook avec vos informations d'identification, effectuera une recherche avec le hashtag spécifié dans le fichier `.env`, puis extraira le contenu des 10 premiers résultats de la recherche. Les résultats seront imprimés dans la console.

## Remarques

- Assurez-vous d'avoir installé la version de ChromeDriver compatible avec votre version de Google Chrome. En cas d'incompatibilité, le script peut ne pas fonctionner correctement.
- Le script utilise la bibliothèque Selenium pour automatiser l'interaction avec le navigateur web. Veuillez respecter les conditions d'utilisation et les politiques des sites web que vous souhaitez scraper.
- Ce script est fourni à titre d'exemple et peut nécessiter des ajustements supplémentaires en fonction de vos besoins spécifiques.
