---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: md,ipynb
    main_language: python
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.1
---

# test

```python
import pandas as pd
df = pd.read_csv("EXP_2025.csv", sep=";")
df["SG_UF_NCM"].value_counts()
len(df)
ncm = pd.read_csv("NCM.csv")
ncm.head()
with open("NCM.csv", "r", encoding="utf-8") as file:
    file.readline()
```


