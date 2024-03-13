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
df_customers["Points"].describe()
# %%
