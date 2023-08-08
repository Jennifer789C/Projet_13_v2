## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- Créer un fichier `.env` pour y indiquer :
```
SECRET_KEY=<la SECRET_KEY de votre projet Django>
```
- `python manage.py collectstatic` pour récupérer les fichiers statiques
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`
- Pour tester la couverture des tests, `pytest --cov`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info
  (oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Sentry

Sentry est une plateforme qui signale automatiquement les erreurs et les 
exceptions du projet. Il permet également la surveillance des performances.

- Créer un compte [Sentry](https://sentry.io/signup/?original_referrer=https%3A%2F%2Fdocs.sentry.io%2F)
- Créer un projet avec la plateforme `Django`
- Récupérer la clé dsn et l'intégrer dans votre fichier .env
```
SENTRY_DSN=<la clé dsn de votre projet Sentry>
```
- Se connecter sur votre compte Sentry pour visualiser les logs récupérés 
  par Sentry
- Aller sur `http://localhost:8000/sentry-debug/` pour générer une 
  ZeroDivisionError


## Développement local via Docker

Docker est une plateforme permettant de lancer des applications en 
utilisant des conteneurs logiciels.

- Créer un compte [DockerHub](https://hub.docker.com/)
- Installer Docker pour [Windows](https://docs.docker.com/desktop/install/windows-install/) ou pour [Mac](https://docs.docker.com/desktop/install/mac-install/)
- Récupérer l'image docker pour exécuter l'application en local, `docker 
  pull jenny789/oc-lettings:latest`
- S'assurer que le serveur local n'est pas en cours d'exécution 
- Lancer le serveur via Docker Compose, `docker-compose up` 
- Le site doit fonctionner de la même façon avec les mêmes urls, qu'en 
  utilisant uniquement Django
- Pour arrêter le serveur sans supprimer les ressources créées : 
  `docker-compose stop`, et pour l'arrêter en détruisant l'ensemble des 
  ressources créées : `docker-compose down`

## Déploiement

Un pipeline CI/CD est mis en place pour le développement et le déploiement 
de cette application. Il est suivi sur la plateforme CircleCI.   
A chaque push sur la branche "main" du repository GitHub, un travail de 
compilation et de tests est lancé. Ensuite, si ce dernier est validé, une image 
Docker de l'application est construite et pusher sur DockerHub. Enfin, si la 
conteneurisation est réussie, l'application est déployée sur Render.

Pour que tout ceci fonctionne correctement, il faut :
- Avoir pushé le repository sur son propre compte GitHub,
- Avoir configuré son compte CircleCI,
- Avoir configuré son compte Render.

### Render

- Créer un compte [Render](https://dashboard.render.com/#) avec GitHub
- Cliquer sur "Nouveau" puis "Web Service"
- Indiquer votre repository GitHub public
- Configurer votre projet en le nommant et en indiquant Docker dans 
  l'option "Runtime". Dans les options avancées, ajouter les variables 
  d'environnement suivantes et indiquer Non dans l'option "Auto-Deploy"

| Variable Render | Description                                       |
|-----------------|---------------------------------------------------|
| SECRET_KEY      | la SECRET KEY de votre projet Django              |
| SENTRY_DSN      | la clé dsn de votre projet Sentry                 |

### CircleCI

- Créer un compte [CircleCI](https://circleci.com/vcs-authorize/?return-to=https%3A%2F%2Fapp.circleci.com%2Fdashboard) 
avec GitHub
- Créer votre projet CircleCI à partir de votre repository GitHub, en 
  sélectionnant l'option "Fastest" et la branche "main"
- Dans les paramètres du projet, onglet Variables d'environnement, ajouter 
  plusieurs variables :

| Variable CircleCI | Description                                       |
|-------------------|---------------------------------------------------|
| SECRET_KEY        | la SECRET KEY de votre projet Django              |
| SENTRY_DSN        | la clé dsn de votre projet Sentry                 |
| DOCKER_USER       | le nom d'utilisateur de votre compte Docker       |
| DOCKER_PASSWORD   | le mot de passe de votre compte Docker            |
| RENDER_URL        | l'url privée de votre projet Render (Deploy Hook) |


Une fois que tout est configuré, un simple push sur la branche main de 
votre repository GitHub suffit à déployer l'application qui sera accessible 
à l'adresse : <nom de votre projet Render>.onrender.com