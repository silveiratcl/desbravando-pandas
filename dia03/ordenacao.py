# %%

import pandas as pd
# %%
df = pd.read_csv("../data/customers.csv", sep = ";")
df

# %%
# ordenar maior -> menor
# ordenar por alfabetico

df.sort_values(by=["Points", "Name"], ascending=[False, True]).tail(10)

# %%
# versão otimizada do sort values

df = (df.sort_values(by=["Points", "Name"],
               ascending=[False, True])
        .rename(columns={"Name":"Nome", "Points":"Pontos"}))
df


# %%
# ordenando valores
df.sort_values(by="Points")
# %%
# não alterao o df, gera um novo ordenado
# se colocar o inplace=True altera o original
df.sort_values(by="Points", ascending=False )
df.rename(columns={"Name":"Nome", "Points":"Pontos"}, inplace=True)
df
# %%
df = (df.sort_values(by="Pontos", ascending=False)
        .rename(columns={"Name":"Nome", "Points":"Pontos"}))
df


# %%
