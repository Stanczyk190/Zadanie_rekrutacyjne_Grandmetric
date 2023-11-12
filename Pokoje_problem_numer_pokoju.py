import pandas as pd
import re

nazwa_pliku = 'wyniki_rekrutacja.xlsx'
df = pd.read_excel(nazwa_pliku)

# Znajdź numery wierszy z problemem w kolumnie room_number
problematyczne_wiersze = []

# Sprawdź czy brak wartości lub numer pokoju powtarza się
mask = df['room_number'].isna() | df.duplicated(subset='room_number', keep=False)
problematyczne_wiersze = (df[mask].index + 2).tolist()

# Wyświetl numery wierszy z problemem
print("Numery wierszy z problemem w kolumnie room_number:", problematyczne_wiersze)

# Wyświetl informacje o liczbie wierszy z problemem
print("Liczba wierszy z problemem:", len(problematyczne_wiersze))