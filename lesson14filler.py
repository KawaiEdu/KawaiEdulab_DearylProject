nilai_murid = {
    ("atha", "matematika"): 85,
    ("atha", "fisika"): 80,
    ("atha", "matamatika"): 79,
    ("atha", "fisika"): 91,
    ("atha", "matematika"): 87,
    ("atha", "fisika"): 100
}

def nilaimurid(scores):
    for (name, subject), scores in scores.items():
        print(f"{name} - {subject}: {scores}")

print("\n--- nilai murid---")
nilaimurid(nilai_murid)

data = {
    "usa": {
        "california": {"la": 10_000_000, "fransisco": 870_000},
        "texas": {"huston": 2_300_000, "dals": 1_300_000},
    },
    "canada": {
        "rio": {"ronto": 2_900_000, "tawa": 1_000_000},
        "british": {"voncer": 630_000},
    },
}

def findpopulasi(data, kota):
    for negara, states in data.items():
        for state, cities in states.items():
            if kota in cities:
                return f"{kota} has a population of {cities[kota]} in {state}, {negara}."
    return f"{kota} not found in the dataset."

print("\n--- searching for city population---")
print(findpopulasi(data, "huston"))
print(findpopulasi(data, "voncer"))
print(findpopulasi(data, "la"))