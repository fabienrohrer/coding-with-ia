# Partie 0: Préparation et objectifs du TP

## 1. Forker le repository

https://github.com/fabienrohrer/tp-ia

> On fork pour pouvoir utiliser les fonctionnalités de gestion de projet (branches, issues, pull requests) et d'intégration continue (actions) dans la deuxième partie du TP.

## 2. Lancer le projet starter

**Etat:** squelette fonctionnel

Réferez vous à `RUN.*.md` pour l'installation et le lancement de l'application.
On veut pouvoir lancer l'application en local et voir le résultat dans un navigateur web.

## 3. Application: état actuel et objectifs

Etat: L’application est aujourd’hui un boilerplate/starter fonctionnel qu’on peut lancer directement, avec une UI minimale affichant un message d’accueil (“Mobilist… add your favorite movies into a list”), un login déjà en place, et une connexion à la base de données validée via un fichier SQL d’initialisation qui crée une table country : cette table et la logique associée (dont une sélection de country côté appli) servent surtout d’exemple technique pour démontrer l’accès aux données, mais ne correspondent pas à l’objectif “films” et sont donc un bon candidat à être retiré/remplacé lors du TP.

**Objectifs** (réalistes en 1h, alignés Copilot au quotidien) :
- Remplacer la logique country par un domaine Movie (table + modèle)
- Afficher la liste des films de l’utilisateur connecté (GET / affichage UI)
- Ajouter un film (POST + formulaire simple)
- Supprimer un film (DELETE)
- Mini revue de code assistée IA : lisibilité, validations simples, noms, duplication
- Automatisation locale : génération de tests (backend ou frontend) ou génération de documentation (README / JavaDoc / Swagger)

Techniquement, on veut:
1. DB + REST API (Movie, endpoints, scoping user)
2. UI (liste + form + delete) (bootstrap)
3. Review IA
4. Tests/doc

**Objectifs Optionnels** (si avance rapide) :
    - Améloritation de l’UI
    - Modifier un film (PUT/PATCH)
    - Champ “vu” et/ou “note” (1–5)
    - Tri / filtre / recherche simple côté UI
    - Intégration API externe pour récupérer des informations sur les films (vraiment bonus)

# Partie 1: Mise en pratique

## Conseils pour le TP:

- Utilisez l’IA en priorité, mais gardez le contrôle : vous lisez, vous validez, vous testez.
- utilsez tout l'éventail de fonctionnalités de votre IA (ex: online chat, chat: agent/ask/plan, ses balises, inline chat, inline suggestions, etc.)
- créez des branches pour chaque grand objectif
- planifiez vos prompts à l'avance (e.g. dans un fichier markdown)
- créez des commits clairs et fréquents pour chaque petite étape réalisée par l'IA
- relisez chaque diff avant de commiter
- relisez ce que l'IA propose avant de l'accepter!
- séquencez les tâches de manière logique (ex: d'abord la partie backend, puis frontend): au besoin, demander de l'aide à l'IA pour planifier les étapes!

### a. Créer un fichier TECHDOC.md

Commencez par demander à l'IA de créer un fichier TECHDOC.md qui contient:

- features actuellement implémentées
- architcture du projet (fichiers principaux et technologies utilisées)
- roadmap (à copier/coller depuis les objectifs du TP)

=> ce document pourra être donné au contexte de chaque prompt et mis à jour au fur et à mesure de l'avancement du projet

> **Solution**: `Agent @project create/update ´/TECHDOC.md´ with sections: features, architecture, roadmap. Describe main files succinctly. Fill features and architecture based on current project state, and roadmap based on TP objectives: ´blah blah´`

=> commit

### b. C'est parti

Itérez pour chaque objectif:
- créer une branche
- préparer une séquence de tâches (Ask IA) 
- Itérez pour chaque tâche:
   - préparer un prompt clair et structuré, contextualisé (fichiers, #web, TECHDOC.md, etc.)
   - relire et valider
   - commiter avec un message clair (proposé par l'IA)
- valider/merger la branche

> Comment s'y prendre? L'API REST en premier? Les tests?
Tous les chemins mènent à Rome, mais certains sont plus rapides que d'autres :-P

# Partie 2: 

