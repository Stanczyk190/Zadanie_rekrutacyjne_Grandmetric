import pandas as pd
import re

nazwa_pliku = 'wyniki_rekrutacja.xlsx'
df = pd.read_excel(nazwa_pliku)

room_number = df['room_number']
qr = df['qr']
measured_temp = df['measured_temp']
issue_heating = df['issue_heating']
issue_motion = df['issue_motion']
issue_temperature_sensor = df['issue_temperature_sensor']
issue_door = df['issue_door']
issue_window = df['issue_window']
issue_heating_switch = df['issue_heating_switch']
issue_kitchen_switch = df['issue_kitchen_switch']
issue_wifi = df['issue_wifi']
problem_description = df['problem_description']
solution = df['solution']
short_uuid = df['short_uuid']


kolumny_problemy = ['issue_heating', 'issue_motion', 'issue_temperature_sensor', 'issue_door',
                    'issue_window', 'issue_heating_switch', 'issue_kitchen_switch', 'issue_wifi', 'problem_description']


licznik_ilosci_problemow = {}

for kolumna in kolumny_problemy:
    ilosc_wiadomosci = df[kolumna].count()
    licznik_ilosci_problemow[kolumna] = ilosc_wiadomosci

# Wyświetl informacje o zliczonych ilościach problemów
for kolumna, ilosc in licznik_ilosci_problemow.items():
    print(f"Ilość problemów typu: '{kolumna}': {ilosc}")

# Zlicz ilość pokoi z przynajmniej jednym problemem
ilosc_pokoi_z_problemem = df[df[kolumny_problemy].notna().any(axis=1)]['room_number'].nunique()

# Wyświetl informację o liczbie pokoi z problemami
print(f"Liczba pokoi z przynajmniej jednym problemem: {ilosc_pokoi_z_problemem}")