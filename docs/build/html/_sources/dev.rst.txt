Développement
=============

Le site présente les éléments présents dans la base de données. Il se
décompose en 3 parties :

    - Home, la page d'accueil,
    - Lettings, une page listant tous les lieux de location,
    - Profiles, une page listant tous les profils utilisateurs.

Les pages "Lettings" et "Profiles" permettent d'accéder aux pages détails
indiquant chaque élément en détail.

Par exemple, la page "Lettings" permet d'accéder à la page indiquant les
détails du lieu "Oceanview Retreat", c'est-à-dire son adresse complète.

Exécuter le site en local avec Django
-------------------------------------

Exécutez les commandes suivantes :

    - ``cd /path/to/Python-OC-Lettings-FR``
    - ``source venv/bin/activate``
    - ``python manage.py collectstatic`` pour récupérer les fichiers statiques
    - ``python manage.py runserver``
    - Aller sur http://localhost:8000 dans un navigateur
    - Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
    - Pour accéder au panel d'administration, aller sur http://localhost:8000/admin
    - Aller sur http://localhost:8000/sentry-debug/ pour générer une ZeroDivisionError et vérifier votre compte Sentry

Exécuter le site en local via Docker
------------------------------------

Docker est une plateforme permettant de lancer des applications en utilisant
des conteneurs logiciels.

Exécutez les commandes suivantes :

    - Créer un compte DockerHub_
    - Installer Docker pour Windows_ ou pour Mac_
    - Récupérer l'image docker pour exécuter l'application en local, ``docker pull jenny789/oc-lettings:latest``
    - S'assurer que le serveur local n'est pas en cours d'exécution
    - Lancer le serveur via Docker Compose, ``docker-compose up``
    - Le site doit fonctionner de la même façon avec les mêmes urls, qu'en utilisant uniquement Django
    - Pour arrêter le serveur sans supprimer les ressources créées : ``docker-compose stop``, et pour l'arrêter en détruisant l'ensemble des ressources créées : ``docker-compose down``

.. _DockerHub: <https://hub.docker.com/>
.. _Windows: <https://docs.docker.com/desktop/install/windows-install/>
.. _Mac: <https://docs.docker.com/desktop/install/mac-install/>

Déployer sur Render
-------------------

Un pipeline CI/CD est mis en place pour le développement et le déploiement de
cette application. Il est suivi sur la plateforme CircleCI.

A chaque push sur la branche "main" du repository GitHub, un travail de
compilation et de tests est lancé. Ensuite, si ce dernier est validé, une image
Docker de l'application est construite et pusher sur DockerHub. Enfin, si la
conteneurisation est réussie, l'application est déployée sur Render.

Pour que tout ceci fonctionne correctement, il faut :

    - Avoir pushé le repository sur son propre compte GitHub,
    - Avoir configuré son compte CircleCI,
    - Avoir configuré son compte Render.

Configurer votre compte Render
______________________________

Exécutez les commandes suivantes :

    - Créer un compte Render_ avec GitHub
    - Cliquer sur "Nouveau" puis "Web Service"
    - Sélectionner votre repository GitHub public
    - Configurer votre projet en le nommant et en indiquant Docker dans l'option "Runtime". Dans les options avancées, ajouter les variables d'environnement suivantes et indiquer Non dans l'option "Auto-Deploy"

+-----------------+--------------------------------------+
| variable Render |              Description             |
+=================+======================================+
|    SECRET_KEY   | la SECRET KEY de votre projet Django |
+-----------------+--------------------------------------+
|    SENTRY_DSN   |   la clé dsn de votre projet Sentry  |
+-----------------+--------------------------------------+

.. _Render: <https://dashboard.render.com/#>

Configurer votre compte CircleCI
________________________________

Exécutez les commandes suivantes :

    - Créer un compte CircleCI_ avec GitHub
    - Créer votre projet CircleCI à partir de votre repository GitHub, en sélectionnant l'option "Fastest" et la branche "main"
    - Dans les paramètres du projet, onglet Variables d'environnement, ajouter plusieurs variables :

+-------------------+---------------------------------------------------+
| Variable CircleCI |                    Description                    |
+===================+===================================================+
|     SECRET_KEY    |        la SECRET KEY de votre projet Django       |
+-------------------+---------------------------------------------------+
|     SENTRY_DSN    |         la clé dsn de votre projet Sentry         |
+-------------------+---------------------------------------------------+
|    DOCKER_USER    |    le nom d'utilisateur de votre compte Docker    |
+-------------------+---------------------------------------------------+
|  DOCKER_PASSWORD  |       le mot de passe de votre compte Docker      |
+-------------------+---------------------------------------------------+
|     RENDER_URL    | l'url privée de votre projet Render (Deploy Hook) |
+-------------------+---------------------------------------------------+

Une fois que tout est configuré, un simple push sur la branche main de votre
repository GitHub suffit à déployer l'application qui sera accessible à
l'adresse : <nom_de_votre_projet_Render>.onrender.com

.. _CircleCI: <https://circleci.com/vcs-authorize/?return-to=https%3A%2F%2Fapp.circleci.com%2Fdashboard>
