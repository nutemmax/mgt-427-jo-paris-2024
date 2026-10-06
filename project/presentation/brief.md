# Brief de présentation

## Objectif

Faire comprendre que la cérémonie d'ouverture de Paris 2024 n'était pas seulement un spectacle. C'était un système de livraison qui devait faire coexister une ambition artistique, un fleuve navigable, des flux de public, des contrôles de sûreté, des secours, une ville active et un signal mondial.

## Public

Le public connaît l'événement, mais pas les méthodes de management de projet et d'analyse des risques. Les diapositives doivent donc introduire les méthodes au moment où elles expliquent un choix du projet. Elles ne doivent pas commencer par un catalogue de définitions.

## Thèse à tester

**La cérémonie a tenu parce que les organisateurs ont traité le site comme un système d'interfaces. Le résultat favorable ne suffit toutefois pas à prouver l'efficacité causale de chaque mesure ni à établir le coût complet du projet.**

Cette thèse s'appuie sur les essais de flotte, le pilotage du niveau d'eau, le plan de mobilité, la protection en profondeur, les options de repli et les limites documentaires.[^1]

## Mode du prototype

Le prototype est un support hybride, de complexité standard. Il suit une lecture linéaire continue. Les schémas, la matrice de risques, les tableaux et les encadrés restent visibles sans interaction obligatoire. Il n'utilise pas d'animation obligatoire ni de dépendance externe. Le thème graphique reste provisoire.

Le prototype suit cinq temps.

1. **Contexte.** Le problème est un spectacle mondial dans une infrastructure urbaine ouverte.
2. **Modèle.** Le système relie fleuve, flotte, public, sécurité, transports et diffusion.
3. **Action.** Le lecteur avance dans le fil et voit le projet passer de la conception aux essais, puis à l'exploitation.
4. **Conséquence.** Les schémas montrent les effets en chaîne et le registre indique le risque résiduel.
5. **Conclusion.** Le projet est analysable, mais les limites de preuve restent visibles.

## Storyboard

| Slide | Question du public | Contenu principal | Visuel ou interaction | Sources de travail |
|---:|---|---|---|---|
| 1 | Quel est le problème ? | Une cérémonie sur six kilomètres, avec une date fixe et plusieurs publics. | Carte conceptuelle du système. | [Périmètre](../context/00-chronologie-perimetre.md#périmètre-retenu). |
| 2 | Pourquoi ce projet est-il différent d'un stade ? | Le fleuve reste une infrastructure active et l'espace public reste habité. | Comparaison enceinte, corridor et interfaces. | [Fleuve](../context/04-meteo-seine-navigation-logistique.md#1-pourquoi-la-seine-change-la-nature-du-projet). |
| 3 | Comment le projet s'est-il construit ? | Concept, direction artistique, tests, jauges, répétitions, exécution. | Chronologie avec points de gel et d'apprentissage. | [Chronologie](../context/00-chronologie-perimetre.md#chronologie-vérifiée). |
| 4 | Qui doit coordonner quoi ? | COJOP, État, préfectures, VNF, transports, artistique, diffuseurs et tiers. | Carte d'interfaces et RACI reconstruit, visibles dans le fil. | [Gouvernance](../context/01-gouvernance-parties-prenantes.md#relations-et-décisions-que-les-sources-permettent-de-suivre). |
| 5 | Où se trouve le risque ? | Débit, pluie, foule, accessibilité, cyber, réputation, finances. | Registre et matrice `R = p × g`. | [Registre de risques](../analysis/03-registre-integre-des-risques.md). |
| 6 | Comment une barrière fonctionne-t-elle ? | Prévision, contrôle, secours, redondance, repli et apprentissage. | Défense en profondeur, visible dans le fil. | [Traitements](../analysis/04-traitements-continuite-apprentissage.md). |
| 7 | Quel résultat peut-on défendre ? | Cérémonie tenue, pluie absorbée, pas d'incident majeur rapporté, mais données incomplètes. | Tableau « établi, soutenu, inconnu », visible dans le fil. | [Lecture critique](../analysis/05-lecture-critique-limites.md). |
| 8 | Quelle leçon emporter ? | Suivre les interfaces, tester les modes dégradés, mesurer les tiers et documenter les décisions. | Checklist de management. | [Cadre](../analysis/00-cadre-et-methode.md). |

## Visuels nécessaires

Le premier prototype utilise des diagrammes SVG et CSS produits dans la page. Les visuels externes restent séparés jusqu'à la décision sur les droits, les crédits et le thème.

| Visuel | Rôle | Données | État |
|---|---|---|---|
| Schéma du système | Montrer les interfaces. | Périmètre des notes de contexte. | Dans le prototype. |
| Chronologie | Montrer les fenêtres d'apprentissage. | `EVENT-*`. | Dans le prototype. |
| Carte des parties prenantes | Montrer les domaines de responsabilité. | `STAKE-*`. | Dans le prototype. |
| Matrice de risque | Prioriser les événements redoutés. | Registre analytique, scores pédagogiques. | Dans le prototype. |
| Défense en profondeur | Montrer les barrières et les dépendances communes. | Mesures documentées et recommandations. | Dans le prototype. |
| Photos de presse | Donner une présence visuelle au récit. | Sources et droits à vérifier. | Hors prototype. |

## Décisions de design différées

Le prototype ne fige pas encore la palette, la typographie, la présence d'images ou le niveau d'animation. Ces décisions doivent être prises après une lecture de la narration et un test sur un écran large et un écran étroit. Le contenu et la hiérarchie restent les contraintes premières.

## Critères d'acceptation du deck

- Le fil de la thèse reste compréhensible sans ouvrir un panneau.
- Chaque score de risque porte la mention « analyse pédagogique ».
- Chaque chiffre important remonte à une note de contexte ou au registre des sources.
- Les faits, inférences et inconnus sont visuellement séparés.
- La lecture reste complète sans ouvrir un panneau ni suivre un lien.
- Le contenu reste lisible sans couleur seule, sans survol et sans animation.
- La page fonctionne sans réseau et sans chemin absolu vers un fichier local.

## Notes

[^1]: [Analyse modulaire](../analysis/README.md) et [registre transversal des sources](../sources/source-register.md).
