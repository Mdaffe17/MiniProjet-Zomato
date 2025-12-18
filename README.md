# Analyse exploratoire des restaurants à Bengaluru (Zomato)

## Description du projet
Ce projet consiste en une analyse exploratoire de données (EDA) du dataset **Zomato Bangalore**,
qui contient plus de 51 000 restaurants répartis dans différents quartiers de Bengaluru.
L'objectif est d'analyser la répartition des restaurants, leurs caractéristiques,
les gammes de prix, les notations et les facteurs de popularité.

Le projet a été réalisé dans le cadre du cours **8PRO408 – Outils de programmation pour la science des données**.

---

## Structure du projet
```
zomato-bangalore-analysis/
│
├── data/
│   └── zomato.csv
│
├── notebook/
│   └── zomato.ipynb
│
├── streamlit/
│   └── app.py
│
├── report/
│   └── rapportfinal.pdf
│
├── README.md
└── requirements.txt
```

---

## Contenu
- **Notebook Jupyter** : analyse exploratoire complète (nettoyage, analyses descriptives, comparaisons, visualisations).
- **Application Streamlit** : mini application interactive présentant plusieurs graphiques.

---

## Installation
Créer un environnement virtuel (optionnel mais recommandé), puis installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Exécution

### Lancer le notebook
```bash
jupyter notebook notebook/zomato.ipynb
```

### Lancer l'application Streamlit
```bash
streamlit run streamlit/app.py
```
---

## Remarques
- Le dataset original est volumineux et a été traité localement avec Pandas.
- Le nettoyage des données est volontairement minimal, conformément aux consignes du projet.
- Les visualisations interactives sont réalisées avec Plotly.

---
## Dataset et application Streamlit
Le dataset Zomato complet (≈574 MB) n’est pas inclus dans le dépôt GitHub en raison des limitations de taille des fichiers.
Les analyses ont été réalisées localement sur le dataset complet, tandis que l’application Streamlit utilise un échantillon représentatif afin de permettre son déploiement.
Le lien officiel pour télécharger le dataset orginal est disponible sur Kaggle:
 https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants
---

## Auteur

MOUCTAR DAFFE

---
Projet réalisé dans un cadre universitaire.
