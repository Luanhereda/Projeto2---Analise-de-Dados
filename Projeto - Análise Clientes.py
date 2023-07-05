#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[1]:


#Passo 1: Importar a base de dados

import pandas as pd
tabela = pd.read_csv("telecom_users.csv")
display(tabela)


# In[2]:


#Passo 2: Entender informações que possuimos e oq tem de errado

tabela = tabela.drop("Unnamed: 0", axis=1) #retirando coluna inutil da tabela (axis para coluna = 1, para linha = 0)
display(tabela)

#tbm é possivel notar valores vazios na tabela que serão resolvidos no proximo passo


# In[3]:


#Passo 3: Tratamento de dados

print(tabela.info()) #descobrir dados que precisam ser tratados
#apagar valores vazios e transformar Dtype necessários


# In[4]:


#Tratamento de dados

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") #coluna totalgasto está como object e deveria ser tratada como Float

tabela = tabela.dropna(how = "all", axis=1)
tabela = tabela.dropna(how = "any" , axis=0)

display(tabela)



# In[5]:


print(tabela["Churn"].value_counts(normalize=True)) #contar valores na coluna "churn"/normaliz=true para mostrar %

#valores condizentes com o passado pela diretoria (26% de cancelamentos)


# ### Conclusões e Ações

# In[6]:


#Passo 5: Como cada coluna da base de dados está impactando na coluna churn? Veremos através de um gráfico comparativo

get_ipython().system('pip install plotly')

import plotly.express as px

for Coluna in tabela.columns:
    grafico = px.hstiogram(tabela, x = Coluna, color = "Churn", text_auto = True, color_discrete_sequence=["purple", "black"])
                          
    grafico.show()
    

#plotly.com/python/histograms/ para edições nos gráficos



Escreva aqui suas conclusões:

 1 - Clientes com contratos mensais cancelam muito mais 
      Solução: Promoções para contratos anuais
      
 2 - Familias maiores tendem a cancelar menos que familia menores/solteiros
      Solução: Fazer promoções para uma linha adicional de telefone
 
 3 - Clientes com pouco tempo com nosso serviço estão cancelado muito mais
     - Primeira experiencia ruim
     - Estrategia de captação de clientes errada
     
     Solução: Incentivo para o cliente se manter como cliente
     
 4 - Quanto menos serviços o cliente possui, maior a taxa de cancelamento
     Solução: Promoções com mais serviços envolvidos

 5 - Cancelamento de quem possui serviço de fibra é muito mais comum que com outros serviços (possivel problema no serviço)
     Solução: Agir sobre a fibra

 6 - Clientes que utilizam boleto eletronico tendem a cancelar mais
     Solução: Ação para migrar clientes para outras formas de pagamento
     
