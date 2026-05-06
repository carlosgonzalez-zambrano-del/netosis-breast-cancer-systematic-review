# netosis-breast-cancer-systematic-review
Pyton codes of netosis-breast-cancer-systematic-review

## How to Reproduce

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the pipeline:

```bash
python scripts/search_pubmed.py
python scripts/clean_data.py
python scripts/prisma_filter.py
python scripts/prisma_strict.py
```

---

## Notes

* Update your email in the PubMed script before running
* Ensure internet connection for API queries
* Outputs will be generated in `data/processed/`
