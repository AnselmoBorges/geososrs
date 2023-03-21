# Databricks notebook source
# MAGIC %md
# MAGIC ## Essse belo notebook faz uma magica
# MAGIC A de te tornar um grande vagabundo, rs

# COMMAND ----------
# importar biblioteca spark
from pyspark.sql.functions import *


# Crie uma função python que busque o CEP
def busca_cep(cep):
  import requests
  import json
  url = "https://viacep.com.br/ws/{}/json/".format(cep)
  response = requests.get(url)
  return json.loads(response.text)

# COMMAND ----------

# Leia o resultado da função e crie um dataframe spark
df = spark.createDataFrame([busca_cep(cep) for cep in ["03978290", "01521000"]])
display(df)