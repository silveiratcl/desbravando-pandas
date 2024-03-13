# %%
import pandas as pd

# %%

idades = [30, 42, 90, 34] #vira uma série
idades

# %%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total / (len(idades) - 1)
variancia

# %%
# Transformação para séries Pandas
# Quando a série data frame é convertido para pandas
# ele já possui os métodos embutidos
# verbos das séries (calcular média, mediana, std)
series_idades = pd.Series(idades)
series_idades

# %%
# Métodos da séries pandas
# Média
series_idades.mean()

# %%
# Variância
series_idades.var()

# Desvio padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# 3o Quartil
series_idades.quantile(0.75)

# %%
# Sumarização
series_idades.describe()

# %%
# Dimensão da série
# isso é uma tupla (4,)
# diz quantas linhas a série possui
series_idades.shape[0]

# %%
# Navegando na lisa
# no índice 0
idades[0]

# %%
# Navegando na série
# indice da série
series_idades[2]

# %%
# Alterando index da série
series_idades.index = ['t', 'e', 'o', 'c']
# %%
# Navegando nos índices novos
series_idades['t']

# %%

series_idades.index = [40, 10, 30, 20]
series_idades

# %%
series_idades

# %%
# index pela posicao
series_idades.iloc[2:4]

# %%
series_idades.iloc[0:2]

# %%
# loc indice similar aos dicionários
series_idades.loc[40]

# %%
series_idades.name = 'idades'
series_idades



# %%
# Cria a serie com nome "idades" no pandas
series_idades = pd.Series(idades, name="idades")
series_idades
# data frames conjundo de series!!!
# %%
