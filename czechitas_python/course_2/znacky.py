books = {"4A2 3000": "František Novák", 
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár", 
    "1P5 5269": "Marta Nováková", 
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}

for znacka, jmeno in books.items():
    if znacka[1] == "P":
        print(jmeno)
