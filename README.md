# python-back
ANTHONIPILLAI JACKSON

# Projet de Gestion de Bibliothèque

Ce projet est une API de gestion de bibliothèque construite avec Django et Django REST Framework. Il permet de gérer les auteurs, livres, catégories, exemplaires, emprunts, commentaires, éditeurs et évaluations.

## Tâches Accomplis

### Fonctionnalités Principales

- [x] **Création du modèle de données**  
  Conception des modèles `Auteur`, `Livre`, `Categorie`, `Exemplaire`, `Emprunt`, `Commentaire`, `Editeur`, et `Evaluation`.

- [x] **Sérialisation des données**  
  Création des sérializers pour chaque modèle afin de gérer la conversion des objets en JSON et vice versa.

- [x] **Mise en place des vues**  
  Création de classes de vues utilisant les ViewSets pour chaque modèle avec la gestion des permissions appropriées.

- [x] **Filtrage et pagination**  
  Ajout de la capacité de filtrer les livres et les commentaires, ainsi que la pagination des résultats.

- [x] **Authentification**  
  Intégration de l'authentification JWT avec Django REST Framework et mise en place des routes nécessaires pour l'obtention des tokens.

- [x] **MDP**  
  MAJ sur les rules des mdp pour que ce soit plus sécuriser.

- [x] **Gestion des permissions**  
  Création de permissions personnalisées pour contrôler l'accès aux différentes actions sur les modèles.

- [x] **Documentation de l'API**  
  Utilisation de `drf_yasg` pour générer automatiquement la documentation Swagger de l'API.

- [x] **Throttling**  
  Mise en place de la limitation de la fréquence des requêtes pour les utilisateurs anonymes et authentifiés.

- [] **OTP**

## Utilisateurs

Le système comprend deux types d'utilisateurs, chacun appartenant à des groupes différents avec des rôles spécifiques :

- **Admin**  
  - **Nom d'utilisateur :** `jackson`  
  - **Mot de passe :** `janialqu`  
  - **Rôles :** A tous les droits, y compris la création, la lecture, la mise à jour et la suppression de tous les modèles.

- **Viewer**  
  - **Nom d'utilisateur :** `viewer`  
  - **Mot de passe :** `@test1234`  
  - **Rôles :** Peut uniquement effectuer des requêtes GET sur les différents modèles.


