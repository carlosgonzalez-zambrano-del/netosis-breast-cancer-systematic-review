import pandas as pd

df = pd.read_csv("prisma_priority.csv")

# palabras que indican rol mecanístico fuerte
strong_keywords = [
    "netosis",
    "neutrophil extracellular traps",
    "nets formation",
    "pad4",
    "dnase",
    "citrullinated histone",
    "h3cit",
    "myeloperoxidase dna",
    "metastasis",
    "tumor progression",
    "invasion",
    "migration"
]

def strong_relevance(title):
    t = str(title).lower()
    score = sum(1 for k in strong_keywords if k in t)
    return score >= 2  # exige al menos 2 coincidencias

df["Strict"] = df["Title"].apply(strong_relevance)

df_strict = df[df["Strict"] == True]

df_strict.to_csv("prisma_strict.csv", index=False)

print("Artículos altamente relevantes:", len(df_strict))
