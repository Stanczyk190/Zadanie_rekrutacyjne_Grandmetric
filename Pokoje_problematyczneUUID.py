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

def compare_uuid(room_number, short_uuid, qr, problematic_rooms):
    # Funkcja usuwająca znaki specjalne ze stringa
    def remove_special_chars(s):
        if isinstance(s, str):
            return re.sub(r'\W+', '', s)
        else:
            return s

    # Porównanie short_uuid i qr
    short_uuid_clean = remove_special_chars(short_uuid)
    qr_clean = remove_special_chars(qr)

    if short_uuid_clean != qr_clean and pd.notna(room_number) and room_number not in problematic_rooms:
        print(f"W pokoju {room_number} nie zgadza się UUID.")
        problematic_rooms.append(room_number)

# Lista do przechowywania informacji o pokojach z problemem UUID
pokoje_z_problemem = []


for i in range(len(df)):
    compare_uuid(room_number[i], short_uuid[i], qr[i], pokoje_z_problemem)

# Wyświetl informacje o liczbie pokoi z problemem i same pokoje
print(f"Liczba pokoi z problemem: {len(pokoje_z_problemem)}")
print("Numery pokoi z problemem:", pokoje_z_problemem)