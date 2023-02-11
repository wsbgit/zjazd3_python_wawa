def czyszczenie(tekst):
    czysty_tekst = tekst.upper().replace(',', '').replace('.', '').replace('(', '').replace(')', '')
    return czysty_tekst

def ile_slow(tekst):
    podzielony_tekst = tekst.split()
    return len(set(podzielony_tekst))

with open ('my_file.txt', 'r') as plik_txt:
    cala_tresc = plik_txt.read()

cala_tresc = czyszczenie(cala_tresc)

print('Liczba slow:', ile_slow(cala_tresc))