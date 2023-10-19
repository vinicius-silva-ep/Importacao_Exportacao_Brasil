import requests
import pandas as pd

def file_download(url, end):
    res = requests.get(url, verify=False)

    with open(end, 'wb') as new_file:
        new_file.write(res.content)
        print(f'File save in {end}')

file_download(
    'https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv',
    'assets/PAIS.csv'
)        

