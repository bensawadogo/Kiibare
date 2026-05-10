# Kiibare — Africa Market Access Intelligence

> 🌍 Plateforme SaaS d'intelligence de marché pour les investisseurs africains.

## 🏗️ Architecture

```
kiibare/
├── backend/                # Django 5 + Django Ninja (API REST)
│   ├── core/               # Configuration Django (settings, urls, wsgi)
│   ├── api/                # Application principale (models, endpoints, schemas)
│   │   ├── management/     # Commandes personnalisées (seed data)
│   │   ├── models.py       # Modèles : UserProfile, BrokerRecommendation, AssetOpportunity
│   │   ├── api.py          # Endpoints API (health, profiles, brokers, opportunities)
│   │   ├── schemas.py      # Schémas Pydantic (validation entrée/sortie)
│   │   └── admin.py        # Interface d'administration Django
│   ├── manage.py           # CLI Django
│   ├── requirements.txt    # Dépendances Python
│   └── Dockerfile
├── frontend/               # Next.js 14 + React + TailwindCSS
│   ├── app/                # Pages (App Router)
│   ├── package.json
│   ├── tailwind.config.js
│   ├── next.config.js
│   └── Dockerfile
├── docker-compose.yml      # Orchestration des 3 services
├── .env.example            # Variables d'environnement (template)
├── ROADMAP.md              # Roadmap fonctionnelle du projet
└── README.md               # Ce fichier
```

- **Frontend :** Next.js 14, React, TailwindCSS (mobile-first, ultra-rapide)
- **Backend :** Django 5 + Django Ninja (Python, API REST auto-documentée)
- **Base de données :** PostgreSQL 15 (idéal pour les données financières)
- **Orchestration :** Docker & Docker Compose

## 🚀 Lancer le projet

### Prérequis
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Démarrage rapide
```bash
# 1. Cloner le dépôt
git clone https://github.com/VOTRE_PSEUDO/kiibare.git
cd kiibare

# 2. Copier les variables d'environnement
cp .env.example .env

# 3. Construire et lancer tous les services
docker-compose up -d --build
```

Le backend applique automatiquement les migrations au démarrage. ✅

### Accéder aux services

| Service | URL | Description |
|---------|-----|-------------|
| 🖥️ Frontend | [http://localhost:3000](http://localhost:3000) | Interface utilisateur Next.js |
| ⚙️ API Docs (Swagger) | [http://localhost:8000/api/docs](http://localhost:8000/api/docs) | Documentation interactive de l'API |
| 🔒 Admin Django | [http://localhost:8000/admin/](http://localhost:8000/admin/) | Panneau d'administration |
| 🗄️ PostgreSQL | `localhost:5432` | Base de données (DBeaver/PgAdmin) |

### Insérer des données de démo
```bash
docker-compose exec backend python manage.py seed
```

### Créer un super-utilisateur (pour accéder à /admin/)
```bash
docker-compose exec backend python manage.py createsuperuser
```

## 📡 Endpoints API

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/api/health` | Vérification que l'API tourne |
| `POST` | `/api/profiles` | Créer un profil investisseur |
| `GET` | `/api/profiles` | Lister les profils |
| `GET` | `/api/profiles/{id}` | Récupérer un profil |
| `GET` | `/api/brokers` | Lister les courtiers recommandés |
| `GET` | `/api/brokers/top?limit=5` | Top courtiers par score |
| `GET` | `/api/opportunities` | Lister les opportunités |
| `GET` | `/api/opportunities/high-confidence?min_score=7.0` | Opportunités haute confiance |

## 🛠️ Commandes utiles

```bash
# Voir les logs d'un service
docker-compose logs -f backend
docker-compose logs -f frontend

# Entrer dans le conteneur backend
docker-compose exec backend bash

# Arrêter le projet
docker-compose down

# Reconstruire après modification d'un Dockerfile
docker-compose up -d --build
```

## 📄 Licence

Ce projet est propriétaire. Tous droits réservés.
