import pandas as pd
import os

INPUT = "../data/raw/pubmed_results.csv"
OUTPUT_DIR = "../data/processed"
OUTPUT = os.path.join(OUTPUT_DIR, "clean_results.csv")

# crear carpeta si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# cargar datos
df = pd.read_csv(INPUT)

print(f"Artículos iniciales: {len(df)}")

# eliminar sin DOI
df = df[df["DOI"].notna() & (df["DOI"].astype(str).str.strip() != "")]
print(f"Con DOI: {len(df)}")

# eliminar duplicados por DOI
df = df.drop_duplicates(subset="DOI")
print(f"Sin duplicados: {len(df)}")

# clasificar especie
def classify_species(title):
    title = str(title).lower()
    if any(x in title for x in ["dog", "canine", "bitch"]):
        return "canine"
    elif any(x in title for x in ["human", "patient", "women", "female"]):
        return "human"
    else:
        return "unspecified"

df["Species"] = df["Title"].apply(classify_species)

# guardar
df.to_csv(OUTPUT, index=False)

print("Archivo limpio guardado en data/processed/")
