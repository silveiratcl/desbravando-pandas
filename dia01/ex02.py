# Converta o seguinte dicionário para DataFrame e obtenha:

# sumário de cada coluna
# média da coluna idade
# ultimo nome da coluna nome

# dados = {"nome":["Teo", "Nah", "Napoleão"], "idade": [31, 32, 14] }

# %%
import pandas as pd

# %%
dados = {"nome":["Teo", "Nah", "Napoleão"], "idade": [31, 32, 14]}
# %%
df = pd.DataFrame(dados)

# %%
sumario_numericas = df.describe()
df["nome"].describe()
# %%
# ultimo nome da coluna nome
df["nome"].iloc[-1]
# %%
df["idade"].mean( )

# %%
