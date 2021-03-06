{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "dd1e87ce",
   "metadata": {},
   "source": [
    "# <center>Partie 1 : Base de données, Analyse, Prétraitement et Préparation</center>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "467b518f",
   "metadata": {},
   "source": [
    "## traitement des fichiers csv"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e3a304c",
   "metadata": {},
   "source": [
    "> le traitement initial des fichiers est fait dans le fichier 'import_fichiers'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05ec8e3e",
   "metadata": {},
   "source": [
    "## traitement de données"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9bf269a",
   "metadata": {},
   "source": [
    "### importer les bibliothèques de base, les autres seront importées au fur et à mesure"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3ff3ca36",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3105cf80",
   "metadata": {},
   "source": [
    "#### import du fichier csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "046db124",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('data.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "99761507",
   "metadata": {},
   "source": [
    "#### premières visualisations du jeu de données"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "76b33fb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Q1</th>\n",
       "      <th>Q2</th>\n",
       "      <th>Q3</th>\n",
       "      <th>Q4</th>\n",
       "      <th>Q5</th>\n",
       "      <th>Q6</th>\n",
       "      <th>Q7</th>\n",
       "      <th>Q8</th>\n",
       "      <th>Q9</th>\n",
       "      <th>Q10</th>\n",
       "      <th>Score</th>\n",
       "      <th>Interpretation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>a</td>\n",
       "      <td>a</td>\n",
       "      <td>a</td>\n",
       "      <td>a</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>b</td>\n",
       "      <td>b</td>\n",
       "      <td>b</td>\n",
       "      <td>b</td>\n",
       "      <td>b</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>c</td>\n",
       "      <td>c</td>\n",
       "      <td>c</td>\n",
       "      <td>c</td>\n",
       "      <td>c</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>20</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>c</td>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>8</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>b</td>\n",
       "      <td>c</td>\n",
       "      <td>a</td>\n",
       "      <td>c</td>\n",
       "      <td>a</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>11</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9 Q10  Score Interpretation\n",
       "0  a  a  a  a  a  1  1  1  1   1     10              B\n",
       "1  b  b  b  b  b  2  2  2  2   2      0              C\n",
       "2  c  c  c  c  c  3  3  3  3   3     20              A\n",
       "3  a  b  c  a  b  1  2  3  1   2      8              C\n",
       "4  b  c  a  c  a  3  2  3  1   2     11              B"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "363e6bbd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 225 entries, 0 to 224\n",
      "Data columns (total 12 columns):\n",
      " #   Column          Non-Null Count  Dtype \n",
      "---  ------          --------------  ----- \n",
      " 0   Q1              217 non-null    object\n",
      " 1   Q2              213 non-null    object\n",
      " 2   Q3              212 non-null    object\n",
      " 3   Q4              215 non-null    object\n",
      " 4   Q5              211 non-null    object\n",
      " 5   Q6              213 non-null    object\n",
      " 6   Q7              215 non-null    object\n",
      " 7   Q8              213 non-null    object\n",
      " 8   Q9              215 non-null    object\n",
      " 9   Q10             217 non-null    object\n",
      " 10  Score           225 non-null    int64 \n",
      " 11  Interpretation  225 non-null    object\n",
      "dtypes: int64(1), object(11)\n",
      "memory usage: 21.2+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5860eddb",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = data.copy()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a97a5bd1",
   "metadata": {},
   "source": [
    "#### Traitement des données non numériques\n",
    "> remplacement des valeurs non-souhaitées par des 'Nan'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f5926c4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# remplacer les caractères a,b,c par des 1, 2, 3, les autres sont automatiquement convertis en nan \n",
    "\n",
    "caracteres_rempla_abc = {\n",
    "    'a':'a',\n",
    "    'b':'b',\n",
    "    'c':'c',\n",
    "    'A':'a',\n",
    "    'B':'b',\n",
    "    'C':'c'    \n",
    "}\n",
    "for colonne in range(0,5):\n",
    "    df.iloc[:,colonne] = df.iloc[:,colonne].map(caracteres_rempla_abc)\n",
    "\n",
    "\n",
    "\n",
    "# remplacer les caractères 'string' 1,2,3 par des 1, 2, 3, les autres sont automatiquement convertis en nan \n",
    "caracteres_rempla_123 = {\n",
    "    '1':'a',\n",
    "    '2':'b',\n",
    "    '3':'c' \n",
    "}\n",
    "for colonne in range(5, 10):\n",
    "     df.iloc[:,colonne] = df.iloc[:,colonne].map(caracteres_rempla_123)\n",
    "        \n",
    "# label encoder 'a la main' de la colonne interpretation\n",
    "caracteres_rempla_target = {\n",
    "    'A':0,\n",
    "    'B':1,\n",
    "    'C':2\n",
    "}\n",
    "df['Interpretation'] = df['Interpretation'].map(caracteres_rempla_target)\n",
    "\n",
    "caracteres_rempla = {\n",
    "    'a':0,\n",
    "    'b':1,\n",
    "    'c':2\n",
    "}\n",
    "for colonne in range(0,10):\n",
    "    df.iloc[:,colonne] = df.iloc[:,colonne].map(caracteres_rempla)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "03866a1e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Q1                float64\n",
       "Q2                float64\n",
       "Q3                float64\n",
       "Q4                float64\n",
       "Q5                float64\n",
       "Q6                float64\n",
       "Q7                float64\n",
       "Q8                float64\n",
       "Q9                float64\n",
       "Q10               float64\n",
       "Score               int64\n",
       "Interpretation      int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# vérification du type des données\n",
    "df.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a8477d1",
   "metadata": {},
   "source": [
    "vérification"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "af6a40e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Q1</th>\n",
       "      <th>Q2</th>\n",
       "      <th>Q3</th>\n",
       "      <th>Q4</th>\n",
       "      <th>Q5</th>\n",
       "      <th>Q6</th>\n",
       "      <th>Q7</th>\n",
       "      <th>Q8</th>\n",
       "      <th>Q9</th>\n",
       "      <th>Q10</th>\n",
       "      <th>Score</th>\n",
       "      <th>Interpretation</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>20</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>8</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>11</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Q1   Q2   Q3   Q4   Q5   Q6   Q7   Q8   Q9  Q10  Score  Interpretation\n",
       "0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0     10               1\n",
       "1  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0      0               2\n",
       "2  2.0  2.0  2.0  2.0  2.0  2.0  2.0  2.0  2.0  2.0     20               0\n",
       "3  0.0  1.0  2.0  0.0  1.0  0.0  1.0  2.0  0.0  1.0      8               2\n",
       "4  1.0  2.0  0.0  2.0  0.0  2.0  1.0  2.0  0.0  1.0     11               1"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# visualisation du jeu de données pour vérifier la transformation\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dee4546f",
   "metadata": {},
   "source": [
    "##### choix de suppression des NaN, par rapport au remplacement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d81266c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "34002d9f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(41, 12)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6bda6210",
   "metadata": {},
   "source": [
    "> Ré-indexer le dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9eab7c38",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "425cfaf8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    29\n",
       "1    11\n",
       "0     1\n",
       "Name: Interpretation, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# voir les données présentes par interprétation\n",
    "df['Interpretation'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6b2d721",
   "metadata": {},
   "source": [
    "#### écartement des colonnes 'score' et 'interprétation' pour créer le jeu de données des features "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c36d0437",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = df.drop(columns=['Score','Interpretation'], axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8cc6f586",
   "metadata": {},
   "source": [
    "#### choix  : prédire le score ; l'interprétation est écartée du jeu de données"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "dbc6535b",
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df['Interpretation']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a1e28a5",
   "metadata": {},
   "source": [
    "#### séparation du jeu de données en donnée de test et d'entrainement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5e59f239",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cae073f6",
   "metadata": {},
   "source": [
    "# <center>KNN from scratch</center>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "44dd5ef8",
   "metadata": {},
   "source": [
    "Création des fonctions pour le calcul de différentes distances\n",
    "\n",
    "> utilisation des np.array pour utiliser le calcul matriciel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "de124951",
   "metadata": {},
   "outputs": [],
   "source": [
    "def euclidien(row1, row2):\n",
    "       \n",
    "    row1 = np.array(row1)\n",
    "    row2 = np.array(row2)\n",
    "    \n",
    "    row1 = row1.reshape(row1.shape[0], 1)\n",
    "    row2 = row2.reshape(row2.shape[0], 1)\n",
    "    \n",
    "    res = (row1 - row2)**2\n",
    "    res = sum(res)\n",
    "    res = np.sqrt(res)\n",
    "    res = np.around(res,2)\n",
    "    \n",
    "    return res\n",
    "\n",
    "\n",
    "def manhattan(row1, row2):\n",
    "    \n",
    "    row1 = np.array(row1)\n",
    "    row2 = np.array(row2)\n",
    "    \n",
    "    row1 = row1.reshape(row1.shape[0], 1)\n",
    "    row2 = row2.reshape(row2.shape[0], 1)\n",
    "    \n",
    "    \n",
    "    return sum(abs(row1 - row2))\n",
    "\n",
    "\n",
    "def minkowski(row1, row2, p):\n",
    "        \n",
    "    row1 = np.array(row1)\n",
    "    row2 = np.array(row2)\n",
    "    \n",
    "    row1 = row1.reshape(row1.shape[0], 1)\n",
    "    row2 = row2.reshape(row2.shape[0], 1)\n",
    "    \n",
    "    res  = sum((row1 - row2)**p)\n",
    "    res = res**(1/p)\n",
    "    res = np.around(res,decimals=2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "092d1972",
   "metadata": {},
   "source": [
    "création de la fonction distance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "34a2bcc7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def distance(row, dataframe, method='euclidien', p=3):\n",
    "    \n",
    "    liste = {}\n",
    "       \n",
    "        \n",
    "    for ligne_test in range(X_test.shape[0]):\n",
    "        \n",
    "        liste2 = []\n",
    "        \n",
    "        for ligne in range(dataframe.shape[0]):\n",
    "            \n",
    "            if method == 'euclidien':\n",
    "\n",
    "                res = euclidien(X_test.iloc[ligne_test], X.iloc[ligne])\n",
    "            \n",
    "            if method == 'manhattan':\n",
    "                \n",
    "                res = manhattan(X_test.iloc[ligne_test], X.iloc[ligne])\n",
    "                \n",
    "            if method == 'minkowski':\n",
    "                \n",
    "                res = minkoswki(X_test.iloc[ligne_test], X.iloc[ligne], p=p)\n",
    "\n",
    "            liste2.append(res[0])\n",
    "        \n",
    "        mon_nom_de_colonne = str(ligne_test)\n",
    "        mon_nom_de_colonne = 'col' + mon_nom_de_colonne\n",
    "        \n",
    "        liste[mon_nom_de_colonne] = liste2\n",
    "    \n",
    "    \n",
    "    \n",
    "    return liste\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6b5f512b",
   "metadata": {},
   "source": [
    "#### pour chaque ligne des X, calculer la distance entre toutes les lignes et une seule ligne\n",
    "\n",
    "utilisation de dataframes pour les résultats pour faciliter la lecture dans jupyter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "503e836c",
   "metadata": {},
   "outputs": [],
   "source": [
    "res_euclidien = pd.DataFrame(distance(X.iloc[0], X_train))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e71d0a2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col0</th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "      <th>col3</th>\n",
       "      <th>col4</th>\n",
       "      <th>col5</th>\n",
       "      <th>col6</th>\n",
       "      <th>col7</th>\n",
       "      <th>col8</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.00</td>\n",
       "      <td>4.00</td>\n",
       "      <td>4.12</td>\n",
       "      <td>0.00</td>\n",
       "      <td>6.32</td>\n",
       "      <td>3.16</td>\n",
       "      <td>3.61</td>\n",
       "      <td>3.46</td>\n",
       "      <td>4.12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.45</td>\n",
       "      <td>2.45</td>\n",
       "      <td>2.24</td>\n",
       "      <td>3.16</td>\n",
       "      <td>3.16</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2.24</td>\n",
       "      <td>2.45</td>\n",
       "      <td>2.24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.00</td>\n",
       "      <td>4.00</td>\n",
       "      <td>3.61</td>\n",
       "      <td>6.32</td>\n",
       "      <td>0.00</td>\n",
       "      <td>3.16</td>\n",
       "      <td>4.12</td>\n",
       "      <td>4.47</td>\n",
       "      <td>3.61</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.24</td>\n",
       "      <td>3.74</td>\n",
       "      <td>2.65</td>\n",
       "      <td>3.46</td>\n",
       "      <td>4.47</td>\n",
       "      <td>2.45</td>\n",
       "      <td>3.00</td>\n",
       "      <td>2.83</td>\n",
       "      <td>2.65</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.24</td>\n",
       "      <td>2.65</td>\n",
       "      <td>3.46</td>\n",
       "      <td>4.36</td>\n",
       "      <td>3.87</td>\n",
       "      <td>2.65</td>\n",
       "      <td>3.46</td>\n",
       "      <td>3.61</td>\n",
       "      <td>3.74</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   col0  col1  col2  col3  col4  col5  col6  col7  col8\n",
       "0  4.00  4.00  4.12  0.00  6.32  3.16  3.61  3.46  4.12\n",
       "1  2.45  2.45  2.24  3.16  3.16  0.00  2.24  2.45  2.24\n",
       "2  4.00  4.00  3.61  6.32  0.00  3.16  4.12  4.47  3.61\n",
       "3  4.24  3.74  2.65  3.46  4.47  2.45  3.00  2.83  2.65\n",
       "4  2.24  2.65  3.46  4.36  3.87  2.65  3.46  3.61  3.74"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "res_euclidien.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "12b1aacc",
   "metadata": {},
   "outputs": [],
   "source": [
    "res_manhattan = pd.DataFrame(distance(X.iloc[0], X_train, method='manhattan'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "f9afb2ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col0</th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "      <th>col3</th>\n",
       "      <th>col4</th>\n",
       "      <th>col5</th>\n",
       "      <th>col6</th>\n",
       "      <th>col7</th>\n",
       "      <th>col8</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>20.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   col0  col1  col2  col3  col4  col5  col6  col7  col8\n",
       "0  10.0  10.0  11.0   0.0  20.0  10.0   9.0   8.0  11.0\n",
       "1   6.0   6.0   5.0  10.0  10.0   0.0   5.0   6.0   5.0\n",
       "2  10.0  10.0   9.0  20.0   0.0  10.0  11.0  12.0   9.0\n",
       "3  10.0  10.0   7.0   8.0  12.0   6.0   7.0   6.0   7.0\n",
       "4   3.0   7.0   8.0  11.0   9.0   7.0   8.0   9.0  10.0"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "res_manhattan.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "4b81f68e",
   "metadata": {},
   "outputs": [],
   "source": [
    "res_minkoswki = pd.DataFrame(distance(X.iloc[0], X_train, method='manhattan', p=5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7f46cc89",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col0</th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "      <th>col3</th>\n",
       "      <th>col4</th>\n",
       "      <th>col5</th>\n",
       "      <th>col6</th>\n",
       "      <th>col7</th>\n",
       "      <th>col8</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>20.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>6.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>20.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>12.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>11.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>9.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   col0  col1  col2  col3  col4  col5  col6  col7  col8\n",
       "0  10.0  10.0  11.0   0.0  20.0  10.0   9.0   8.0  11.0\n",
       "1   6.0   6.0   5.0  10.0  10.0   0.0   5.0   6.0   5.0\n",
       "2  10.0  10.0   9.0  20.0   0.0  10.0  11.0  12.0   9.0\n",
       "3  10.0  10.0   7.0   8.0  12.0   6.0   7.0   6.0   7.0\n",
       "4   3.0   7.0   8.0  11.0   9.0   7.0   8.0   9.0  10.0"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "res_minkoswki.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af8444c3",
   "metadata": {},
   "source": [
    "#### création de la fonction de prédiction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "02850cc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "\n",
    "def predict(df_fit, k):\n",
    "    \n",
    "    liste = []\n",
    "    \n",
    "    for i in df_fit.columns:\n",
    "\n",
    "        df_nn = df_fit.sort_values(by=i)[:k]\n",
    "\n",
    "        # Create counter object to track the labels\n",
    "\n",
    "        counter = Counter(y[df_nn.index])\n",
    "\n",
    "        # Get most common label of all the nearest neighbors\n",
    "\n",
    "        liste.append(counter.most_common()[0][0])\n",
    "\n",
    "    return liste"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8cdf2b70",
   "metadata": {},
   "outputs": [],
   "source": [
    "# mettre les résultats en dictionnaire\n",
    "y_pred_liste = {}\n",
    "y_pred_liste['minkoswski'] = (predict(res_minkoswki, 4))\n",
    "y_pred_liste['manhattan'] = (predict(res_manhattan, 4))\n",
    "y_pred_liste['euclidien'] = (predict(res_euclidien, 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "bb2c4ef1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "minkoswski : 0.8888888888888888\n",
      "manhattan : 0.8888888888888888\n",
      "euclidien : 0.7777777777777778\n"
     ]
    }
   ],
   "source": [
    "# affichage des résultats\n",
    "from sklearn.metrics import accuracy_score\n",
    "for nom, pred in zip(y_pred_liste.keys(), y_pred_liste.values()):\n",
    "    \n",
    "    score = accuracy_score(y_test, pred)\n",
    "    \n",
    "    print(f'{nom} : {score}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4dd895df",
   "metadata": {},
   "source": [
    "#### création de graphique pour la visualisation des différentes prédictions par rapport aux données réelles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "311acc95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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0vrbpD1pTi3jE2EAOZBaF06ePKl3v/vdE15z2223aedO769l9913n3p7e3NVXmGp3+hNp0x3alnkgFRaKS3kGBUEz7Q7h5xzD07zeNa7/Ai35eu9cfbnTh3wuZLMS00q21A/w1jZuV7JjRErA5BxP/jBDzR//nzddNNNkrzm0P3336/m5mafKwupllbpWx+STr4srZxm91BXalJZXU5KA1DYVqxYoW984xvTXrdjx45pr8EctLRKP/hvUt8pqXrZ1Nd27fMaSkwqQwDxXyWybv6CGkVUo5Kew36XknHt3QMqKynSikUVM3tiPObdEisD8saRI0e0adMmffCDH9Tll1+u973vffq///f/6uabb1ZTU5NeeOEFvfDCC7rpppt09dVX66abbtKBA17T/LHHHtO73vUubdu2TU1NTfr93//9C177D//wD3XVVVfphhtu0OnTpyVJTz31lK6//npdffXVeutb36rTp0/ryJEjeuSRR/Q//+f/1JYtW/TDH/5QTz75pD72sY9py5YtOnz4sP7xH/9R1157ra666ir9p//0nxSPxyVJ73//+/WRj3xEN910k9avX5/WXzgKwsb7pKKS9D4VjhwgUgZgSv/8z/+s6667Tlu2bNFv/uZvanR09IIdot/4xjf0/ve/X5J0+vRpvfOd79RVV12lq6666oJdoZK37lx+ufchbCKR0Pbt23XllVfqve99rxKJxPnr1q1bp+7u7kl/vuTtRpporUEamlslOW+AwXRYJxBgNIeQE11lq1Xdf9TvMjLucGRA62orVVw0w1x0ItkcYucQkFcOHTqk3/3d39Wrr76q/fv361/+5V/04x//WH/913+tv/zLv9SmTZv03HPP6Re/+IX+7M/+TJ/85CfPP3fXrl362te+pt27d+trX/uajh8/LkkaGBjQDTfcoFdeeUW33HKL/vEf/1GS9OY3v1nPP/+8fvGLX2j79u36q7/6K61bt04PP/ywfu/3fk+7du3Srbfeqne84x36zGc+o127dmnDhg1617vepRdffFGvvPKKNm/erC984Qvna+js7NSPf/xjffvb39bHP/7x3P7DC6rKxV60bO8TU0fLnJMi+6UlvOkHMLF9+/bpa1/7mn7yk59o165dKi4u1pe//OVJr//IRz6iW2+9Va+88opefvlltbS0THrt5z//eVVWVurVV1/VH/7h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SZKkwtQyi0MZKC8vZ926daxevZr6+nqOPvpounfvzpYtW5gwYQJVVVUUFRWxatUq1q5dy/HHH7+97+zZs5k9ezbl5eUANDQ0sGzZsn0Wh771rW9tfz5o0CDGjh3LpZdeyiWXXLLH9qeffjolJSXb7/n3v/+dyspKADZu3MiyZcuazdJccai56wwYMIArr7ySLVu2MHLkSPr27ZvHpyhJkiRJkgpNyywO7WWEz8E0atQoKisr+eCDDxg9ejTQtBNYfX09CxcupLi4mBNPPJFNmzbt1C+lxC233MK111670/m6ujo+//zz7ce79jviiCO2P7/nnnt47bXXmDlzJn379mXJkiUcc8wxzbZPKfGb3/yG4cOH79Rm1qxZe8zSnOauA1BVVcXMmTO5/PLLGT9+PFdccUVe15QkSZIkSYXDNYf2w+jRo3nssceorKxk1KhRQNNIms6dO1NcXMyrr77KihUrdus3fPhwpk2bRkNDAwCrVq1i3bp1HHfccaxbt47169ezefNmnnvuuWbv/c477zBw4EDuuOMOjj32WFauXLnXrMOHD2fKlCls2bIFgLfffpuPP/642Sz7e50VK1bQuXNnvv/973PVVVexaNGiveaRJEmSJEmFqWWOHMpI7969+eijj+jatStdunQBYMyYMVx00UX079+fvn370rNnz936nXfeedTU1HDmmWcCTVvGP/zww3Tu3JnbbruNgQMHUlJSsse+24wfP55ly5aRUmLYsGGcdtppe8169dVXU1tbS79+/Ugp0alTJ5555pm9Ztmf68yZM4c777yT4uJijjzySB566KG8PkNJkiRJklRYIqWUdYbd9O/fPy1YsGCnczU1NZx66qkZJdIX4XcmHXgRsTCl1D/rHJIkSZJaD6eVSZIkSZIktWEWhyRJkiRJktowi0OSJEmSJEltWIsqDhXi+kjaM78rSZIkSZJahhZTHOrQoQPr16+36NACpJRYv349HTp0yDqKJEmSJEnahxazlX23bt2oq6ujvr4+6yjKQ4cOHejWrVvWMSRJkiRJ0j60mOJQcXExJSUlWceQJEmSJElqVVrMtDJJkiRJkiQdeBaHJEmSJEmS2jCLQ5IkSZIkSW1YFOLuXxFRD6z4Al2PBT48wHEOhELMZab8FWIuM+WvEHN9mUz/llLqdCDDSJIkSWrbCrI49EVFxIKUUv+sc+yqEHOZKX+FmMtM+SvEXIWYSZIkSVLb5bQySZIkSZKkNszikCRJkiRJUhvW2opDU7MO0IxCzGWm/BViLjPlrxBzFWImSZIkSW1Uq1pzSJIkSZIkSfuntY0ckiRJkiRJ0n5oNcWhiDg/It6KiOUR8dOs8wBExLSIWBcRb2SdZZuI+GpEvBoRNRHxZkT8uAAydYiI6oj4n1ymn2WdaZuIaBcRiyPiuayzbBMRtRHxekQsiYgFWecBiIiOEVEZEUtzv60zM87z9dzns+3vnxFxQ5aZcrluzP3G34iIP0dEh6wzSZIkSVKrmFYWEe2At4H/AOqA+cC3U0r/yDjXYKABeCilVJpllm0iogvQJaW0KCL+BVgIjMzys4qIAI5IKTVERDEwD/hxSulvWWXaJiJuAvoDR6WULsw6DzQVh4D+KaUPs86yTUT8EZibUrovIg4BDk8pbcg4FrD9vw+rgIEppRUZ5uhK02+7V0rp04h4HHg+pfRgVpkkSZIkCVrPyKHTgeUppXdTSp8BjwEXZ5yJlFIV8L9Z59hRSmlNSmlR7vlHQA3QNeNMKaXUkDsszv1lXrWMiG7ABcB9WWcpZBFxFDAYuB8gpfRZoRSGcoYB72RZGNpBe+CwiGgPHA6szjiPJEmSJLWa4lBXYOUOx3VkXPBoCSLiRKAceC3jKNumby0B1gEvpZQyzwTcBfwE+DzjHLtKwOyIWBgR12QdBugB1AMP5Kbg3RcRR2QdagejgT9nHSKltAqYDLwPrAE2ppRmZ5tKkiRJklpPcSj2cC7zkSeFLCKOBJ4Ebkgp/TPrPCmlrSmlvkA34PSIyHQaXkRcCKxLKS3MMkczBqWU+gEjgB/mpi9mqT3QD5iSUioHPgYKZd2vQ4AK4IkCyHI0TSMaS4ATgCMi4rJsU0mSJElS6ykO1QFf3eG4G07XaFZuXZ8ngUdSSk9lnWdHuelIc4Dzs03CIKAit77PY8C/R8TD2UZqklJanXtcBzxN07TKLNUBdTuM9qqkqVhUCEYAi1JKa7MOApwLvJdSqk8pbQGeAs7KOJMkSZIktZri0Hzg5IgoyY0UGA3MyDhTQcot/nw/UJNS+q+s8wBERKeI6Jh7fhhN/xO9NMtMKaVbUkrdUkon0vR7+u+UUuajPCLiiNxC4uSmbp0HZLobXkrpA2BlRHw9d2oYkOli8Dv4NgUwpSznfeCMiDg89+9wGE1rfkmSJElSptpnHeBASCk1RsQ4YBbQDpiWUnoz41hExJ+Bc4BjI6IOuD2ldH+2qRgEXA68nlvjB2BCSun57CLRBfhjblepIuDxlFLBbB1fYI4Dnm6qLdAeeDSl9GK2kQC4HngkV5x9F/hexnmIiMNp2sHw2qyzAKSUXouISmAR0AgsBqZmm0qSJEmSWslW9pIkSZIkSfpiWsu0MkmSJEmSJH0BFockSZIkSZLaMItDkiRJkiRJbZjFIUmSJEmSpDbM4pAkSZIkSVIbZnFIkiRJkiSpDbM4JEmSJEmS1IZZHJIkSZIkSWrD/g/4oUU+YeWHBgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1440x720 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(20,10))\n",
    "\n",
    "plt.subplot(1,3,1)\n",
    "plt.plot(predict(res_minkoswki, 4), label=\"minkowski\")\n",
    "plt.plot(np.array(y_test), label=\"valeurs réelles\")\n",
    "plt.legend()\n",
    "\n",
    "plt.subplot(2,3,2)\n",
    "plt.plot(predict(res_manhattan, 4), label = \"manhattan\")\n",
    "plt.plot(np.array(y_test), label=\"valeurs réelles\")\n",
    "plt.legend()\n",
    "\n",
    "plt.subplot(2,3,3)\n",
    "plt.plot(predict(res_euclidien, 4), label=\"euclidien\")\n",
    "plt.plot(np.array(y_test), label=\"valeurs réelles\")\n",
    "plt.legend()\n",
    "\n",
    "plt.savefig('scratch.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25a0391b",
   "metadata": {},
   "source": [
    "# <center>KNN from Sklearn</center>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce7c01ed",
   "metadata": {},
   "source": [
    "import des bibliothèques"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "5ef73c55",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neighbors import KNeighborsClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "b114f536",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6682f256",
   "metadata": {},
   "source": [
    "#### création des paramètres pour gridSearchCv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "491ab9e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# création d'une liste de différentes valeurs de k\n",
    "k_range = list(range(1, 15))\n",
    "\n",
    "# mettre ces paramètres dans un dictionnaire à faire passer dans gridSearchCv\n",
    "param_grid = dict(n_neighbors=k_range)\n",
    "\n",
    "# ajout d'une ligne avec différentes valeurs de p dans le dictionnaire\n",
    "param_grid['p'] = [1, 2, 3]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "225ae32a",
   "metadata": {},
   "source": [
    "#### création d'un modèle Knn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "1bcd26c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "clf2 = KNeighborsClassifier()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec43b913",
   "metadata": {},
   "source": [
    "#### recherche des meilleurs paramètres en fonction du dictionnaire passé"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c92e6f09",
   "metadata": {},
   "outputs": [],
   "source": [
    "grid = GridSearchCV(clf2, param_grid, cv=5, scoring='accuracy', return_train_score=False,verbose=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "7b3784c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 5 folds for each of 42 candidates, totalling 210 fits\n"
     ]
    }
   ],
   "source": [
    "grid_search = grid.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "09cfc81b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'n_neighbors': 4, 'p': 1}\n"
     ]
    }
   ],
   "source": [
    "# voir les meilleurs paramètres\n",
    "print(grid_search.best_params_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "05781549",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8095238095238095"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# visualiser l'accuracy \n",
    "accuracy = grid_search.best_score_ \n",
    "accuracy"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f53d000",
   "metadata": {},
   "source": [
    "#### création du modèle avec les bons paramètres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "1daf0558",
   "metadata": {},
   "outputs": [],
   "source": [
    "clf_def = KNeighborsClassifier(n_neighbors=4, p=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "75189e5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier(n_neighbors=4, p=1)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf_def.fit(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "60adac7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7777777777777778"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf_def.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d76d3b24",
   "metadata": {},
   "source": [
    "# exportation du modèle créé"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "1f6282d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['regression_model_saved.joblib']"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from joblib import dump\n",
    "\n",
    "dump(clf_def, 'regression_model_saved.joblib')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7305daf3",
   "metadata": {},
   "source": [
    "> <h1>la suite se passe en exécutant le fichier run.py !</h1>"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
