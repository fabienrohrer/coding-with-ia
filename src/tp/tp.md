# Partie 0: Préparation et objectifs du TP

## 1. Forker le repository

https://github.com/fabienrohrer/tp-ia

> On fork pour pouvoir utiliser les fonctionnalités de gestion de projet (branches, issues, pull requests) et d'intégration continue (actions) dans la deuxième partie du TP.

## 2. Lancer le projet starter

**Etat:** squelette fonctionnel

Réferez vous à `RUN.*.md` pour l'installation et le lancement de l'application.
On veut pouvoir lancer l'application en local et voir le résultat dans un navigateur web.

## 3. Application: état actuel et objectifs

Etat: L’application est aujourd’hui un boilerplate/starter fonctionnel qu’on peut lancer directement, avec une UI minimale affichant un message d’accueil (“add your favorite movies into a list”), un login déjà en place, et une connexion à la base de données validée via un fichier SQL d’initialisation qui crée une table country : cette table et la logique associée (dont une sélection de country côté appli) servent surtout d’exemple technique pour démontrer l’accès aux données, mais ne correspondent pas à l’objectif “films” et sont donc un bon candidat à être retiré/remplacé lors du TP. Il faut vérifier si la test suite est opérationnel.

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

# Partie 1: Mise en pratique / solo

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

> **Solution**: `Agent @project create/update ´/TECHDOC.md´ with sections: features, architecture, technologies (dependencies). Describe main files succinctly. Fill features and architecture based on current project state.`

=> commit

### b. Créer une roadmap

Créer un fichier ROADMAP.md avec les objectifs du TP, séparés en grandes étapes (PR) et sous-étapes (commits).
Essayer de la penser comme si vous deviez coder vous même les fonctionnalités.

=> commit

> Comment s'y prendre? L'API REST en premier? Les tests? La création de la base de données? L'UI?
Tous les chemins mènent à Rome, mais certains sont plus rapides que d'autres :-P

> Utiliser Ask, inline suggestions et/ou Github Copilot Web. Simplifier/structurer à la main.

### c. C'est parti

Itérez pour chaque objectif:
- créez une branche
- préparez une séquence de tâches (Ask IA) 
- Itérez pour chaque tâche:
   - préparez un prompt clair et structuré, contextualisé (fichiers, #web, TECHDOC.md, etc.)
   - relisez et validez
   - commitez avec un message clair (proposé par l'IA)
- validez/mergez la branche

> N'acceptez que des PRs testés, relues et simplifiées!

### d. Alternative: l'outil "Plan"

"Plan" permet sans doute de faire tout ce qui précède en une fois de manière plus automatisée.
Mais c'est à double tranchant: plus rapide, mais moins de contrôle et de granularité.


# Partie 2: Mise en pratique / collaboratif


## a. Ajouter .github/copilot-instructions.md

**À quoi sert ce fichier ?**

´/.github/copilot-instructions.md´ est un fichier d’instructions persistantes (en Markdown) qui donne à GitHub Copilot le contexte projet et les règles d’équipe à appliquer “par défaut” (style, architecture, sécurité, tests, commandes, etc.). Il sert à aligner Copilot sur vos standards, afin d’obtenir des propositions plus cohérentes et directement utilisables.

> Objectif : peu de texte, très actionnable (Copilot est probabiliste : vous “biaisiez” ses choix, vous ne le “verrouillez” pas).

- Project overview : 2–4 lignes sur ce que fait l’app et les règles métier clés
- Tech stack : backend, frontend, tests, outils (versions si utiles)
- Build / run / test : commandes exactes et chemins importants
- Coding guidelines : simplicité, conventions, validations minimales, pas de dépendances inutiles
- Sécurité de base : pas de secrets, data scoppée à l’utilisateur connecté (anti cross-user)
- Attendu qualité : “si feature => au moins 1 test OU procédure de vérif manuelle”

**Quand est-il utilisé ?**

Dès que vous utilisez Copilot sur ce repo, les instructions peuvent être prises en compte pour :
- Copilot Chat (dans l’IDE et sur GitHub.com)
- Copilot code review (revue PR)
- Copilot coding agent (agent)

#### Example

```markdown
# GitHub Copilot instructions (team)

## Project context
- Stack: Java (backend) + Angular (frontend)
- Goal: "movie list" app, data always scoped to the currently authenticated user

## Build & test
- Backend: run `mvn test` and `mvn spring-boot:run`
- Frontend: run `npm test` and `npm start`

## Coding rules
- Prefer simple, readable code; avoid broad refactors unless necessary
- Follow existing naming and package/module structure
- Add minimal validations (null/empty, simple bounds)
- Do not introduce unnecessary dependencies
- Always include how to test (command + nominal test case)

## API / security (baseline)
- Never log secrets or tokens
- Ensure every read/write is scoped to the current user (no cross-user leakage)

## Quality bar
- For any new/changed feature: add at least 1 test OR a short manual verification checklist
```

=> créez un fichier `.github/copilot-instructions.md` avec des instructions claires et actionnables pour aligner Copilot sur les standards de votre projet.
=> commitez le dans la branche main


## b. Revue de code assistée par IA

> Objectif : expérimenter une revue de code collaborative avec Copilot : vous créez une PR, Copilot est reviewer, vous discutez et itérez ensemble.

- inventez une feature un minimum complexe (ex: champ “vu” + filtre “vu/non vu”)
- implémentez la feature comme dans la partie 1
- Créez une PR github
- Demandez à l'IA de faire une revue de code de la PR.
    - Dans la PR GitHub (en haut à droite), demandez à copilot d'être Reviewer de la PR.
- Analysez ses commentaires, discutez avec elle, et demandez-lui d'implémenter les changements qu'elle propose.
- En local, vérifiez les changements proposés.
- Itérer au moins deux fois.
- Validez/mergez la PR.

### c. Cloud Agent

> Objectif : expérimenter un mode "asynchrone" : vous déléguez une tâche, Copilot travaille dans le cloud, crée une branche + une draft PR, pousse des commits, puis vous demande une revue. Vous restez responsable : vous relisez, demandez des changements, puis vous mergez (ou refusez).

### Exercice

Choisissez une petite tâche.

#### Option A: depuis GitHub.com

1) Dans le repo GitHub, ouvrez le panneau "Agents".
2) Demander l'implémentation de la tâche.
   - Exemple : `Add an "About" page with a funny description of the project.`
3) Copilot crée une *draft PR* et travaille dedans.
4) ☕

#### Option B : depuis IntelliJ

1) Ouvrez Copilot Chat.
2) Décrivez la même tâche.
3) Cliquez **Delegate to Coding Agent**.
4) ☕

### Revue & itération (le cœur "collaboratif")

1) Lisez la PR comme une PR d’un collègue : diff, cohérence, tests, risques.
2) Demandez une itération directement dans la PR :
    - Ajoutez un commentaire qui demande une modification (exemples ci-dessous).
3) Refaites une 2e review après la nouvelle itération.

Prompts de commentaires (à copier/coller dans la PR) :

- `@copilot Please simplify this change: keep only the README section and remove any refactor.`
- `@copilot Add a short manual test checklist in the PR description (3 bullets max).`
- `@copilot Ensure user data is scoped to the authenticated user and add a minimal validation.`
