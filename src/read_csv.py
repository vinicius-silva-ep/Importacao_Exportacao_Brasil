import pandas as pd

# Ler o arquivo CSV e criar um DataFrame
df = pd.read_csv('assets/PAIS.csv', sep=';', encoding='ISO-8859-1', quotechar='"')

# Ver o dataframe
print(df.head())
