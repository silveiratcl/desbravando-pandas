#Converta a seguinte lista de dados para series pandas e obtenha:
# media
# devio padrão
# máximo valor

# dados = [ 10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

# %%
import pandas as pd
# %%
dados = [ 10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
series_dados = pd.Series(dados)
# %%
media = series_dados.mean()
# %%
desvio = series_dados.std()
# %%
maximo = series_dados.max()

# god safe
