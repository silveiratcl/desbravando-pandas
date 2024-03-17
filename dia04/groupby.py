# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%
# agregação pela condição "IdCustomer"

condicao = df["IdCustomer"]=="5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user['Points'].sum()

# %%
# por função fazendo a soma por id
pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df["IdCustomer"]==i
    pontos[i] = df[condicao]["Points"].sum()

pontos

# %%
# usando pandas
# agregação por operação soma, media....

df_summary = df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index() # reset index é o índice do df que é atualizado

# %%

# Recencia
# valor
# Frequencia
# ultima data
# a logica segue a mesma do dplyr em R, começa pelos dados e
# e vai piping/pipeline os dados nas funções, muito daora
# groupby sempre com operações
# distincti e unique quando não tem, em SQL


(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum', ##agregate
          "UUID": "count",
          "DtTransaction": "max"})
    .rename(columns={ #renomeando as colunas
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())

# %%
import datetime

data1 = df["DtTransaction"][0]
now = datetime.datetime.now()

(now - data1).days

# %%

(datetime.datetime.now() - df["DtTransaction"][0]).days

# %%
def recencia(x): # serie do df x todas as datas
    diff = datetime.datetime.now() - x.max() # now - DtTransactiom
    return diff.days # retorna em dias


(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": ['max', recencia] # passando a função e o max
          }) # fazendo o double check no df
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())
# %%
