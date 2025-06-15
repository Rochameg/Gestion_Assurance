STRUCTURE DU PROJET
/mon_projet_flask/
│
├── app/ # Dossier principal de l'application
│ ├── **init**.py # Initialise l'app Flask, les extensions, etc.
│ ├── routes.py # Routes principales de l'application
│ ├── models.py # Modèles de base de données (SQLAlchemy)
│ ├── forms.py # Formulaires Flask-WTF
│ ├── templates/ # Fichiers HTML (Jinja2)
│ │ ├── layout.html
│ │ ├── index.html
│ │ └── ...
│ └── static/ # Fichiers statiques : CSS, JS, images, etc.
│ ├── css/
│ ├── js/
│ └── images/
│
├── migrations/ # Dossier de migration de base de données (Flask-Migrate)
│
├── venv/ # Environnement virtuel Python (peut être ignoré par git)
│
├── config.py # Fichier de configuration (clé secrète, DB URI, etc.)
├── run.py # Point d’entrée pour lancer l’app
├── requirements.txt # Dépendances Python
└── README.md # Documentation du projet
