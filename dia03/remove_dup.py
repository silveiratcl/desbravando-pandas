# %%
import pandas as pd

data = {
    "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
    "Idade": [32,33,2,33,32,32],
    "updated_at": [1,2,3,1,2,3]
}

# %%

df = pd.DataFrame(data)

# garante que coloca o mais atual ordenado por primeiro
df = df.sort_values(by="updated_at", ascending = True)
df = df.drop_duplicates(subset = ["Nome", "Idade"], keep='first')
df
# %%
# otimizado
df = (df.sort_values(by="updated_at", ascending = False)
        .drop_duplicates(subset = ["Nome", "Idade"], keep='first'))
df

# %%
