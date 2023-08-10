Install
=======

.. _Installation:

Installation
------------

Pour installer le code de cette application, vous devez disposer au
préalable d'un compte GitHub, le Git CLI, le SQLite3 CLI et un interpréteur
Python avec une version 3.6 ou supérieure.

Une fois que vous vous êtes assuré d'avoir chacun de ces prérequis,
l'installation se fait en plusieurs étapes, et dépend de votre OS.

.. note::

    Si vous utilisez Windows et PowerShell, les commandes seront les
    mêmes que celles présentées ci-dessous sauf :

        - pour activer l'environnement virtuel : ``.\venv\Scripts\Activate.ps1``
        - remplacer ``which <my-command>`` par ``(Get-Command <my-command>).Path``

Cloner le repository GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exécutez les commandes suivantes :

    - ``cd /path/to/put/project/in``
    - ``git clone https://github.com/Jennifer789C/Projet_13_v2.git``

Créer l'environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exécutez les commandes suivantes :

    - ``cd /path/to/Python-OC-Lettings-FR``
    - ``python -m venv venv``
    - ``apt-get install python3-venv`` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
    - Activer l'environnement ``source venv/bin/activate``
    - Confirmer que la commande ``python`` exécute l'interpréteur Python dans l'environnement virtuel ``which python``
    - Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure ``python --version``
    - Confirmer que la commande ``pip`` exécute l'exécutable pip dans l'environnement virtuel, ``which pip``
    - Pour désactiver l'environnement, ``deactivate``

Exécuter le site
~~~~~~~~~~~~~~~~
