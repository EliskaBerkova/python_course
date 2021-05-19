schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1, 
  "Matematika": 1, 
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělešná výchova": 3,
  "Chemie": 4,
}
total = 0

for predmet, znamka in schoolReport.items():
    total += znamka
    if znamka == 1:
        print(predmet)

prumerna_znamka = total/len(schoolReport)
print(f"Prumerna znamka je: {prumerna_znamka}")