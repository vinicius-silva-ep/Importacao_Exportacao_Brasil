import csv
import json

# Caminho do arquivo CSV
csv_file_path = 'C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023/IMP_COMPLETA/IMP_COMPLETA.csv'
# Caminho onde o arquivo JSON será salvo, incluindo o nome do arquivo
json_file_path = 'C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023/IMP_COMPLETA/IMP_COMPLETA.json'

# Lista para armazenar os dados
data = []

# Leitura do arquivo CSV
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Convertendo cada linha do CSV em um dicionário
    for row in csv_reader:
        data.append(row)

# Escrita no arquivo JSON
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f'Arquivo JSON criado com sucesso em: {json_file_path}')