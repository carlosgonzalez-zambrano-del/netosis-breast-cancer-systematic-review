import pandas as pd

df = pd.read_csv("../data/processed/clean_results.csv")

keywords = [
    "netosis", "nets", "neutrophil extracellular",
    "metastasis", "microenvironment",
    "tumor progression", "invasion",
    "circulating tumor", "immune"
]

def is_relevant(title):
    t = str(title).lower()
    return any(k in t for k in keywords)

df["Relevant"] = df["Title"].apply(is_relevant)

df_sorted = df.sort_values(by="Relevant", ascending=False)

df_sorted.to_csv("../data/processed/prisma_priority.csv", index=False)

print("Archivo generado: prisma_priority.csv")
print(df["Relevant"].value_counts())
