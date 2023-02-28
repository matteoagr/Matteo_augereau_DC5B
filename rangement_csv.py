import pandas as pd   # Importe la bibliothèque pandas 

df = pd.read_csv('EXO_PYTHON.csv')  # Lit le fichier CSV 'EXO_PYTHON.csv' 

df = df[['Period', 'Data_value', 'Series_title_2']]  # Sélectionne les colonnes 'Period', 'Data_value' et 'Series_title_2' 

df = df.dropna()   # Supprime les lignes contenant des valeurs manquantes

df = df[df['Series_title_2'].isin(['Credit', 'Debit', 'Services'])]  # Filtre pour ne conserver que les lignes où la colonne 'Series_title_2' contient les valeurs 'Credit', 'Debit' ou 'Services'

df['ID'] = range(1, len(df) + 1)  # Crée une nouvelle colonne appelée 'ID' avec des valeurs allant de 1 au nombre de lignes dans le DataFrame

df.to_csv('result.csv', index=False)   # Enregistre le DataFrame filtré dans un nouveau fichier CSV appelé 'result.csv', sans inclure la colonne d'index.


