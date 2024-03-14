# %%

import pandas as pd

# %%

df = pd.read_csv("../data/products.csv",
                 sep = ";",
                 header = None,
                 names = ["Id", "Name", "Description"])
# %%
df
# %%
# exercício
# 1. renomear dataframe df
# 2. renomear "nome" e "descrição"

df2 = df
df2 = df.rename(columns = {"Name": "Nome",
                         "Description": "Descrição"})

df2

# %%
