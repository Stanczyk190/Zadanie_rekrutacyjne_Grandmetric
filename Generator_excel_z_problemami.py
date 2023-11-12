import pandas as pd

nazwa_pliku_wejsciowego = 'wyniki_rekrutacja.xlsx'
nazwa_pliku_wyjsciowego = 'pokoje_z_problemem.xlsx'

df = pd.read_excel(nazwa_pliku_wejsciowego)


kolumny_problemy = ['issue_heating', 'issue_motion', 'issue_temperature_sensor', 'issue_door',
                    'issue_window', 'issue_heating_switch', 'issue_kitchen_switch', 'issue_wifi', 'problem_description']

# Wybierz tylko wiersze z przynajmniej jednym problemem
df_z_problemem = df[df[kolumny_problemy].notna().any(axis=1)]

# Zapisz do nowego pliku Excel
df_z_problemem.to_excel(nazwa_pliku_wyjsciowego, index=False)

print(f"Utworzono plik Excel '{nazwa_pliku_wyjsciowego}' z pokojami z przynajmniej jednym problemem.")