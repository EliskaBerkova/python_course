soucet = 0
for cislo in [1, 2, 4, 8, 10]:
  soucet += cislo
print(soucet)

znamky = [
    ['Petr', 2],
    ['Roman', 1],
    ['Jitka', 3],
    ['Zuzana', 5],
    ['Ondřej', 2],
    ['Julie', 2],
    ['Karel', 4],
    ['Anna', 1],
    ['Eva', 1]
]
soucet = 0
for radek in znamky:
  soucet = soucet + radek[1]
  # soucet += radek[1]
prumer = soucet / len(znamky)
prumer = round(prumer, 2)
print(prumer)

# Výpis studentů, co mají 4 nebo 5
for radek in znamky:
  if radek[1] >= 4:
    print(radek[0])
