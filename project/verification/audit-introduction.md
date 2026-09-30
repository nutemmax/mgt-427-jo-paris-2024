# Audit de la fiche « Introduction au management de projet »

## Périmètre et méthode

J'ai comparé les 35 pages de `slides/1_MGT_427_intro_26.pdf` à `lecture-notes/01-introduction-au-management-de-projet.md` et à la section « Introduction au management de projet » de `lecture-notes/source-map.md`. Chaque page du PDF a été examinée par extraction du texte et par rendu visuel. Les numéros de ligne ci-dessous renvoient à la fiche, sauf mention de la cartographie. J'ai contrôlé les calculs de l'exemple multicritère, les 35 lignes du tableau de couverture, les appels de notes, les URL et la présence d'images locales.

Le document sépare correctement le contenu visible sur les diapositives, les compléments sourcés et les lectures pédagogiques. Aucun passage examiné ne prétend restituer une explication orale du professeur. Les 35 diapositives ont une ligne de couverture, sans omission ni doublon. Les 23 notes appelées sont toutes définies et aucune définition n'est orpheline. Les trois diagrammes Mermaid ont chacun une clôture de bloc. L'exemple multicritère est arithmétiquement juste : `4,0`, `3,5` et `2,8`.

## Constats à corriger

### Majeur 1. La taille de l'enquête PMI est trop proche du graphique sans sa base propre

- **Fiche :** § 6, lignes 189 à 197. **PDF :** diapositive 28.
- **Preuve :** la fiche rapporte correctement la question « projets commencés durant les douze derniers mois, jugés en échec » et les pourcentages `39 %`, `37 %` et `35 %`. Elle ajoute « 5 402 professionnels interrogés pour l'étude globale » juste avant d'interpréter ce graphique. Le [rapport PMI 2018](https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/pulse-of-the-profession-2018.pdf/) imprime bien `5,402 professionals surveyed` en ouverture, mais son texte annonce `4 455` praticiens, `447` cadres et `800` directeurs de PMO, dont la somme vaut `5 702`. Surtout, l'annexe p. 25 ne donne pas une base propre pour la question des causes parmi les projets jugés en échec. La taille globale ne doit donc pas être lue comme le dénominateur du graphique.
- **Correction précise :** conserver la question, la possibilité de trois réponses et les pourcentages. Retirer la phrase sur `5 402` de ce paragraphe, ou la placer dans une remarque séparée qui indique l'incohérence interne du rapport et précise que la base de cet item n'est pas publiée à cet endroit. Ne calculer ni intervalle de confiance ni nombre de répondants à partir de `5 402`.

### Majeur 2. Le diagramme PRINCE2 est nommé, mais ses relations ne sont pas expliquées

- **Fiche :** § 5, lignes 179 à 183. **PDF :** diapositive 27. **Cartographie :** ligne 57.
- **Preuve :** la fiche énumère correctement les sept processus. Le visuel distingue toutefois quatre niveaux, du management d'entreprise ou de programme jusqu'à la livraison par l'équipe, et montre des autorisations, des rapports de fin d'étape, des remontées d'exception et la boucle entre contrôle d'étape et livraison des produits. Ces relations sont précisément ce que le texte extrait du PDF ne restitue pas. Le texte actuel ne permet pas de suivre le flux d'une étape ni de savoir qui autorise sa poursuite.
- **Correction précise :** ajouter un petit diagramme ou une capture lisible de la diapositive avec une légende. Décrire une traversée complète : la direction autorise une étape, le chef de projet la contrôle, l'équipe livre les produits, puis le rapport de fin d'étape et le plan de l'étape suivante reviennent à la direction pour décision. Signaler que le diagramme reproduit une version antérieure, alors que la phrase sur PeopleCert concerne PRINCE2 7.

### Majeur 3. Une des deux URL HERMES de la note 12 est inaccessible

- **Fiche :** note `[^12]`, ligne 310 ; appuis aux lignes 50, 99 et 175.
- **Preuve :** l'URL HERMES Online du « Prologue » renvoie `404 Not Found` lors du contrôle. L'ancien PDF HERMES cité dans la même note est indexé, mais son téléchargement direct a produit une erreur du lecteur web ; son accessibilité reste incertaine. Le [manuel officiel HERMES 2022](https://www.hermes.admin.ch/_Resources/Persistent/d/a/f/e/dafe02dcf0da5987c1347b4a901be568ce65babe/HERMES-gestion-de-projet.pdf) a été ouvert et contient les phases classiques et agiles ainsi que la clôture.
- **Correction précise :** remplacer la seconde URL par une page HERMES vérifiée ou la supprimer. Remplacer l'ancien lien PDF par le manuel officiel accessible ci-dessus, en gardant l'édition 2022 et en donnant la section ou la page précise qui soutient les affirmations sur les rôles et les phases.

### Mineur 1. Les dimensions périphériques de la figure IPMA restent difficiles à retrouver

- **Fiche :** § 2, lignes 53 à 56. **PDF :** diapositive 8.
- **Preuve :** les trois familles comportementale, technique et contextuelle sont exactes. Le texte ne cite que quelques domaines du pourtour de l'œil ; celui-ci comprend aussi, entre autres, comptabilité, bases de données et technologies de l'information, recherche opérationnelle et compétences relationnelles. Aucun visuel local de cette page n'est inséré dans la fiche.
- **Correction précise :** ajouter un petit tableau à trois colonnes qui distingue les trois familles de la figure et donne deux ou trois libellés périphériques par famille, ou une capture légendée suffisamment nette pour lire ces mots. Conserver la distinction déjà faite entre les libellés du support et ceux d'ICB4.

### Mineur 2. La première étape du « brown paper » perd une consigne visible

- **Fiche :** § 4, ligne 131. **PDF :** diapositive 20.
- **Preuve :** l'étape 1 est intitulée « Brainstorming (par niveau hiérarchique) ». La fiche décrit le recueil et le regroupement, mais omet cette précision sur la composition des groupes. Le support ne détaille pas pourquoi les niveaux sont séparés.
- **Correction précise :** ajouter « le visuel propose d'abord un brainstorming par niveau hiérarchique » et présenter l'intérêt éventuel de cette séparation comme une hypothèse pédagogique, pas comme une intention orale attribuée au cours.

### Mineur 3. La gestion des connaissances disparaît de la lecture des phases

- **Fiche :** § 3, lignes 95 à 101. **PDF :** diapositive 17.
- **Preuve :** « Management de la connaissance » figure sous les idées, concepts de réalisation et méthodes de comparaison. La fiche couvre les autres étapes mais ne reprend pas ce point.
- **Correction précise :** ajouter une phrase sur la conservation des hypothèses, variantes rejetées, décisions et résultats de contrôle. Relier cette mémoire à la comparaison des variantes et au transfert de clôture, sans prétendre que le support impose un dispositif documentaire précis.

### Mineur 4. La matrice impact–effort est décrite sans ses quatre positions

- **Fiche :** § 5, ligne 151. **PDF :** diapositive 23.
- **Preuve :** les quatre noms anglais et leurs traductions sont exacts. Le texte ne dit pas quel quadrant correspond à un impact élevé ou faible et à un effort élevé ou faible. C'est pourtant la relation portée par la photographie du tableau.
- **Correction précise :** ajouter une matrice `2 × 2` ou quatre correspondances : *quick wins* = impact fort, effort faible ; *major projects* = impact fort, effort fort ; *fill ins* = impact faible, effort faible ; *hard slogs* = impact faible, effort fort. Conserver la réserve sur la mesure de l'impact et sur les groupes d'usagers.

### Mineur 5. Le score de l'exemple multicritère demande une limite méthodologique

- **Fiche :** § 3, lignes 103 à 113. **PDF :** diapositives 13 et 14.
- **Preuve :** les trois calculs sont exacts et les valeurs sont clairement fictives. La somme pondérée de notes `1` à `5` suppose néanmoins que la différence entre `1` et `2` a le même sens que celle entre `4` et `5`, et que les critères peuvent se compenser. Le support ne fixe ni ce barème ni ces hypothèses.
- **Correction précise :** ajouter une phrase après le tableau : « Ce score est un outil de discussion fondé sur un barème construit ; il ne mesure pas une utilité objective et peut masquer une contrainte éliminatoire. » L'analyse de sensibilité déjà mentionnée reste pertinente.

### Mineur 6. Trois pages humoristiques sont réduites à leur message général

- **Fiche :** § 6, lignes 207 à 213. **PDF :** diapositives 30, 31, 33 et 34.
- **Preuve :** la fiche interprète prudemment les dessins et ne leur attribue aucune valeur statistique. Elle ne relie cependant pas les vignettes de la diapositive 30 aux trois libellés « objectifs clairs et partagés », « collaboration » et « planification, suivi-contrôle ». La diapositive 31 oppose notamment la description du client, la conception, la réalisation, la documentation et l'objet réellement souhaité. Les diapositives 33 et 34 placent les réactions satiriques aux six étapes nommées, du cahier des charges à la mise en œuvre.
- **Correction précise :** ajouter une phrase par illustration ou une petite table « visuel → risque de coordination → outil utile ». Pour la balançoire, donner deux écarts concrets entre demande, réalisation et besoin. Pour les diapositives 33 et 34, montrer que l'ajout « identification, quantification, maîtrise » répond à la dérive représentée ; éviter de présenter la caricature comme une chronologie type. Une capture des diapositives 31 ou 33 n'est utile que si sa légende explicite ces écarts.

### Mineur 7. La cartographie attribue au graphique PMI un millésime absent du rendu

- **Cartographie :** `lecture-notes/source-map.md`, ligne 58. **PDF :** diapositive 28. **Fiche :** ligne 189.
- **Preuve :** la cartographie indique « PMI, 2014 visible sur le rendu ». La diapositive montre `2018` près du logo PMI et reproduit le graphique du [rapport *Pulse of the Profession 2018*](https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/pulse-of-the-profession-2018.pdf/). La fiche utilise bien 2018.
- **Correction précise :** corriger la cartographie lors d'une prochaine révision et conserver le millésime 2018 dans la fiche. Ce constat ne demande aucune modification de la fiche auditée.

### Mineur 8. La provenance locale du support peut être plus facile à suivre

- **Fiche :** ouverture ligne 3 et notes `[^1]` à `[^9]`, lignes 299 à 307.
- **Preuve :** les citations donnent le nom du PDF et les diapositives, conformément au contrat de recherche. Le PDF se trouve maintenant dans `slides/`, alors que la fiche ne donne que son nom de fichier. Les notes groupent parfois plusieurs diapositives sous un seul renvoi ; le texte les localise heureusement par numéro dans les paragraphes.
- **Correction précise :** écrire une fois `slides/1_MGT_427_intro_26.pdf` dans l'ouverture ou la première note. Garder les renvois groupés lorsque le paragraphe compare réellement plusieurs pages, et donner une page précise pour une lecture qui porte sur un seul visuel.

## Matrice de couverture des 35 diapositives

« Couvert » signifie que la fiche restitue l'idée et le visuel utile sans erreur relevée. « À enrichir » signifie que la page est présente mais qu'un constat ci-dessus précise une correction. Les numéros M et m renvoient respectivement aux constats majeurs et mineurs.

| Diapo | Élément vérifié sur le rendu | Lieu dans la fiche | Verdict |
|---:|---|---|---|
| 1 | Titre, auteur et millésime 2024. | Ouverture, ligne 3. | Couvert. |
| 2 | Trois définitions, unicité, temps et ressources. | § 1, lignes 7 à 11. | Couvert. |
| 3 | États 0 et 1, besoins et mesures. | § 1, lignes 13 à 22. | Couvert. |
| 4 | Définition systémique du management et objectif du cours. | § 1, lignes 24 à 28. | Couvert. |
| 5 | Périmètre et réseau d'acteurs internes et externes. | § 2, lignes 32 à 36. | Couvert. |
| 6 | Maître d'ouvrage, maître d'œuvre, chef, sous-traitance et partenaires. | § 2, lignes 32 à 50. | Couvert. |
| 7 | PDCA et amélioration continue. | § 2, lignes 66 à 70. | Couvert. |
| 8 | Œil IPMA et trois familles de compétences. | § 2, lignes 53 à 56. | À enrichir, m1. |
| 9 | Pilotage, utilisateurs, client et RAD 1991. | § 2, ligne 53 ; § 5, ligne 177. | Couvert. |
| 10 | Hiérarchie croisée avec les projets `x` et `y`. | § 2, lignes 53 à 62. | Couvert. |
| 11 | Organisation traditionnelle, entreprise générale et totale. | § 2, ligne 64. | Couvert. |
| 12 | Coûts cumulés et marge de manœuvre. | § 3, lignes 74 à 78. | Couvert. |
| 13 | Approches, critères, variantes et choix multicritère. | § 3, lignes 74 à 113. | À nuancer, m5. |
| 14 | Analyse du risque et distribution indicative. | § 3, lignes 74 à 78. | Couvert ; l'inférence sur `p.p.` est signalée. |
| 15 | Besoin de plusieurs variantes. | § 3, ligne 80. | Couvert. |
| 16 | Diagnostic, étude, variantes, choix et réalisation. | § 3, lignes 95 à 101. | Couvert. |
| 17 | Chaîne détaillée jusqu'à la clôture et gestion des connaissances. | § 3, lignes 95 à 101. | À enrichir, m3. |
| 18 | État existant, bilan des carences et projets d'amélioration. | § 4, lignes 117 à 121. | Couvert. |
| 19 | Flux du système, input–output et processus. | § 4, lignes 123 à 127. | Couvert. |
| 20 | Quatre moments du brown paper. | § 4, ligne 131. | À préciser, m2. |
| 21 | Six familles PESTEL et branches d'Ishikawa. | § 4, lignes 133 à 145. | Couvert. |
| 22 | SWOT, interne, externe et risques associés. | § 4, lignes 133 à 145. | Couvert. |
| 23 | Quatre quadrants impact–effort. | § 5, ligne 151. | À enrichir, m4. |
| 24 | Plusieurs expansions de SMART. | § 5, lignes 153 à 160. | Couvert. |
| 25 | Méthodes générales, spécialisées et certifications. | § 5, lignes 162 à 166. | Couvert. |
| 26 | Phases prédictives, sprints et ajout ponctuel d'agilité. | § 5, lignes 164 à 177. | Couvert. |
| 27 | Processus PRINCE2 et ses flux de décision. | § 5, lignes 179 à 183. | À enrichir, M2. |
| 28 | Question et barres du graphique PMI 2018. | § 6, lignes 187 à 197. | À corriger, M1 ; cartographie m7. |
| 29 | Facteurs de succès et flèche des outils. | § 6, lignes 199 à 203. | Couvert. |
| 30 | Usages des outils et trois vignettes. | § 6, lignes 205 à 209. | À enrichir, m6. |
| 31 | Dix vignettes de la balançoire et objectif final. | § 6, lignes 207 à 209. | À enrichir, m6. |
| 32 | Caricature de résolution selon les pays. | § 6, ligne 211. | Couvert avec la réserve nécessaire. |
| 33 | Six étapes et réactions satiriques. | § 6, ligne 213. | À enrichir, m6. |
| 34 | Même figure avec identification, quantification et maîtrise. | § 6, lignes 213 à 215. | À enrichir, m6. |
| 35 | Six groupes d'outils communs et flèche de projet. | § 6, lignes 217 à 230. | Couvert. |

## Citations, liens, visuels et lisibilité

Les sources externes sont institutionnelles ou primaires pour les affirmations techniques. Le contrôle direct des 15 URL distinctes des notes `[^10]` à `[^23]` a confirmé l'ouverture de 13 adresses. Le vieux PDF HERMES n'a pas pu être lu directement par le lecteur web, même s'il reste indexé ; la page « Prologue » renvoie 404. La correction est donnée en M3. La page IEC citée pour HAZOP est un index institutionnel qui contient bien IEC 61882:2016, mais un lien direct vers la [notice IEC 61882](https://webstore.iec.ch/en/publication/24321) serait plus précis.

La fiche ne contient aucune image locale, bien qu'elle décrive les 35 pages et fournisse trois diagrammes Mermaid. Ce choix fonctionne pour les schémas simples. Les diapositives 8, 23, 27, 28 et 31 gagnent à être reproduites sous forme de capture nette ou de tableau fidèle, car leurs libellés ou leurs relations portent une part du sens. Une capture sans légende n'améliorerait pas la compréhension.

Le fil de la bibliothèque universitaire reste cohérent et ses nombres sont marqués fictifs. Les paragraphes sont lisibles ; les réserves méthodologiques sur les courbes, les pourcentages PMI et les caricatures sont utiles. La note 12 et l'interprétation de l'échantillon PMI sont les corrections prioritaires avant de considérer la fiche comme prête pour une diffusion autonome.

## Verdict

**Couverture complète, exactitude globalement bonne, révision ciblée nécessaire.** Aucun constat critique, trois constats majeurs et huit constats mineurs. La fiche sert déjà à réviser le cours, mais la base du graphique PMI, le flux du schéma PRINCE2 et la référence HERMES doivent être corrigés ou approfondis avant une publication sans le PDF à côté.
