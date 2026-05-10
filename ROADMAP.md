# Roadmap Kiibare - SaaS Market Access Intelligence

Ce document répertorie les étapes manquantes pour transformer le projet actuel en un SaaS fonctionnel et prêt pour la production.

## 1. Initialisation du Backend (Django) - ✅ TERMINÉ
- [x] Initialiser le projet Django : `django-admin startproject core .`
- [x] Configurer l'application `api` dans `settings.py`.
- [x] Créer les migrations initiales : `python manage.py makemigrations api` (Auto dans docker-compose)
- [x] Appliquer les migrations : `python manage.py migrate` (Auto dans docker-compose)
- [x] API de base fonctionnelle (CRUD Profils, Courtiers, Opportunités)
- [ ] Créer un super-utilisateur : `python manage.py createsuperuser`.

## 2. Authentification & Sécurité
- [ ] Implémenter l'authentification JWT (Django Ninja JWT).
- [ ] Créer les endpoints de Login et Signup.
- [ ] Lier `UserProfile` au modèle `User` de Django.
- [ ] Créer les pages Login/Signup sur le Frontend (Next.js).

## 3. Données & Intelligence
- [ ] Intégrer des sources de données réelles (BRVM, UEMOA).
- [ ] Développer la logique IA pour les scores de confiance (`AssetOpportunity`).
- [ ] Implémenter la logique de recommandation de courtiers (`BrokerRecommendation`).

## 4. Fonctionnalités SaaS
- [ ] Intégrer une passerelle de paiement (Stripe, Flutterwave ou Paystack).
- [ ] Gérer les abonnements (Gratuit vs Premium).
- [ ] Créer un Tableau de bord (Dashboard) utilisateur interactif.

## 5. Intégration & Frontend
- [ ] Connecter le Frontend au Backend via des appels API (`fetch` ou `React Query`).
- [ ] Gérer l'état global de l'application (Zustand ou Redux).
- [ ] Optimiser l'interface pour le mobile.

## 6. Mise en Production
- [ ] Configurer les variables d'environnement (`.env`).
- [ ] Préparer les Dockerfiles pour la production (Multi-stage builds).
- [ ] Configurer Nginx et les certificats SSL.
