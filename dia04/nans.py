# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum() #true 1 false 0

# %%
df.isna()

# %%
df.isna().sum()

# %%
df.isna().mean()

# %%
# substitui

df.fillna({
        "idade": df["idade"].mean(),
        "renda":df["renda"].mean(),
        })

# %%
# tira na em colunas definidas any
# qualquer uma das duas colunas com na a linha é excluida
df.dropna(subset=["idade", "renda"], how='any') #any

# %%

# % tira na em colunas definidas all
# tem que ser obrigatoriamente as duas com Nan para serem retiradas
df.dropna(subset=["idade", "renda"], how='all') #all


# %%
# axis por linha com limite de até 3 na
df.dropna(axis=1, thresh=3)

# %%
df.dropna(axis=1, thresh=all)

# %%
