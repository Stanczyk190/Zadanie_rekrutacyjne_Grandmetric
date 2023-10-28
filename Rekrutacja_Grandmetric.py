import os
import pandas as pd
import json

folder_path = 'task_log'
data_list = []

# Przeglądanie wszystkich plików w folderze
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)

        # otwieranie pliku JSON
        with open(file_path, 'r') as file:
            json_data = json.load(file)

        data_list.append(json_data)

# tworzenie ramki danych z listy danych JSON
df = pd.DataFrame(data_list)

# eksportowanie do pliku Excel
output_excel_file = 'wyniki_rekrutacja.xlsx'
df.to_excel(output_excel_file, index=False)

print(f'Utworzono plik: {output_excel_file}')