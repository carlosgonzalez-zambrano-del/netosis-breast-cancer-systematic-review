from Bio import Entrez
import pandas as pd
import time

Entrez.email = "carlos.gonzalez-zambrano@unesp.br"

query = """
("NETosis" OR "Neutrophil Extracellular Traps" OR NETs)
AND
("breast cancer" OR "mammary tumor")
AND
(human OR canine OR dog)
"""

handle = Entrez.esearch(db="pubmed", term=query, retmax=200)
record = Entrez.read(handle)
id_list = record["IdList"]

results = []

for pmid in id_list:
    try:
        fetch = Entrez.efetch(db="pubmed", id=pmid, retmode="xml")
        data = Entrez.read(fetch)

        if not data.get('PubmedArticle'):
            continue

        art = data['PubmedArticle'][0]
        article = art.get('MedlineCitation', {}).get('Article', {})

        title = article.get('ArticleTitle', "")
        doi = ""

        for iden in art.get('PubmedData', {}).get('ArticleIdList', []):
            if iden.attributes.get('IdType') == 'doi':
                doi = str(iden)

        results.append({
            "PMID": pmid,
            "Title": title,
            "DOI": doi
        })

    except Exception as e:
        print(f"Saltando {pmid}: {e}")

    time.sleep(0.3)

df = pd.DataFrame(results)
df.to_csv("../data/raw/pubmed_results.csv", index=False)

print(f"Listo. Artículos encontrados: {len(df)}")
