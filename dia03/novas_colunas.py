# %%

import pandas as pd
import numpy as np
# %%

df = pd.read_csv("../data/customers.csv", sep=";")
# %%
df["Points_double"] = df["Points"] * 2
df
# %%
df["Points_ratio"] = df["Points_double"] / df["Points"]
# %%
df["Constante"] = None
df
# %%

df["Points_log"] = np.log(df["Points"])


# %%

np.log(df[["Points", "Points_double", "Points_ratio"]])
# %%
# upper case the strings
df["Name"].str.upper()

# %%
# upper case somente nas str antes do "_"

def get_first(nome:str):
    nome = nome.upper() # uppercase
    return nome.split("_")[0] # split names

df["Name_First"] = df["Name"].apply( get_first )
# cria "Name First" apply no df
df
# %%
# lambda função para aplicar de forma rapida
# função anonima!!!
get_t = lambda nome: nome.split("_")[0]
get_t
# %%

def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"

df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df

# %%
df["UUID"].apply( lambda x: x[-3:])


# indicadores de marketing

# %%
data = {
    "nome": ["Teo", "Nah", "Maria", "Lara"],
    "recencia": [1,30,10,45],
    "valor": [100, 2000, 15, 500],
    "frequencia": [2, 5, 1, 15]
}

df_crm = pd.DataFrame(data)

# %%
# Indicadores de Marketing
# Recência - tempo de última compra
# valor - valor total das compras
# frequência - numero de compras

# Criar uma nota para priorizar clientes

## Regras
# Se recência <=10: nota 10
# Se recência  > 10 e < 30: nota 5
# Se recência < 5 : nota 0

# Se valor > 1000: nota 10
# Se valor < 1000 e > 100: nota 5
# Se valor < 100 : nota 0

# Se frequencia >10: nota 10
# Se frequencia < 10 e > 5: nota 5
# Se frequencia < 5 : nota 0


def rfv(row):

    nota = 0

    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota += 0

    if row['valor'] > 1000:
        nota += 10
    elif row['valor'] < 1000 > 100:
        nota += 5
    elif row['valor'] < 100:
        nota += 0

    if row['frequencia'] > 10:
        nota += 10
    elif 5<= row['frequencia'] < 10:
        nota += 5
    elif row['frequencia'] < 5:
        nota += 0
    return nota

# %%
rfv(1,100,2) # ok funciona sem row no indice da coluna
# %%



# %%

df_crm["RFV"] = df_crm.apply(rfv, axis=1) ### eixo axis 1 pegando o idica
df_crm
# %%
