# %%
import pandas as pd

# %%

data = {
    "nome":["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo", "calvo"],
    "idade": [31, 32, 31, 2]
}

#%%
data["idade"][0]

# %%
# convertendo em pandas
df = pd.DataFrame(data)
df
#%%
# df idade chamou a coluna  e iloc a posição 0
# cada coluna é uma série, data frame é um conjunto de séries
df["idade"].iloc[0]

# %%
df['sobrenome'].iloc[0]

# %%
# acessando a posição extraindo uma série
# os índices são os nomes das colunas correspondentes
df.iloc[0]

# %%
# Data frame (PLANILHA) é um conjunto de SERIES(COLUNA)
df['idade']

# %%
# indice é a posição, neste caso ordenamos o df pelos indices fornecidos
df.index=[3,2,1,0]
df
# %%
# ACESSOU O INDICE
df["idade"][0]

# %%
# Indices
df.index

# %%
# nomes das colunas # somente para data frame
df.columns

# %%
df.info(memory_usage='deep')

# %%
df.dtypes

# %%

df['peso'] = [80, 53, 65, 14]

# %%
sumario = df.describe()
sumario
# %%
sumario['peso']['mean']

# %%
df.head(2)

# %%
df.tail(2)
# %%
