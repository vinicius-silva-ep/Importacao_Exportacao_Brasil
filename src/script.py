import requests
import pandas as pd

def file_download(url, end):
    res = requests.get(url, verify=False)

    with open(end, 'wb') as new_file:
        new_file.write(res.content)
        print(f'File save in {end}')

import pandas as pd

# Ler o arquivo CSV e criar um DataFrame
df = pd.read_csv('assets/PAIS.csv', sep=';', encoding='ISO-8859-1', quotechar='"')

# Ver o dataframe
print(df.head())
