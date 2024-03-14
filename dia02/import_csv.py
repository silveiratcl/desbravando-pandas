# %%
import pandas as pd

# %%
df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

# %%
df_customers.shape

# %%
df_customers.info(memory_usage='deep')

# %%
df_customers["Points"].astype(int)

# %%
df_customers["Points"].describe()

# %%
df_customers["Points"].max()

# %%
# maneira de fazer um operação vetorial
# sem a necessidade de fazer um for
condicao = df_customers["Points"] > 1000

# Aplicando filtragem em PANDAS
df_customers[condicao]
# maneira de fazer um operação vetorial
# sem a necessidade de fazer um for

# %%
condicao = df_customers["Points"] == df_customers["Points"].max()
df_customers[condicao]

# %%
# Retorna serie booleana com condição logica
df_customers[df_customers["Points"] == df_customers["Points"].max()]["Name"].iloc[0]

# %%
# otimizando a leitura do chunck acima
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0] #iloc posição loc indice


# %%
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_customers[condicao].describe() #

# %%

a = [1, 2, 3, 4]
b = a.copy() # copia, para alterar sem alterar os dados originais
print(a)
print(b)

b.append(5)
print(a)
print(b)

# Roteiro analise de dados
# SQL - joins no banco usando
# Depois de ter uma tabela você analisa os dados em pandas

# %%
df_customers

# %%

#colunas
df_customers[["UUID", "Name"]]

# %%

colunas = df_customers.columns.tolist() # convertendo para lista
colunas.sort() # para ordenar as lista

df_customers = df_customers[colunas]
df_customers
# %%
# renomear colunas

df_customers = df_customers.rename(columns = {"Name": "Nome",
                               "Points": "Pontos"})
df_customers

# %%

df_customers.rename(columns = {"UUID": "Id"}, inplace = True)
df_customers


