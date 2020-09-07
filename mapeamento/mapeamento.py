# -*- coding: utf-8 -*-
"""Mapeamento.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/170BJp91oQhw3iCMHDsPfctIlCXpsSFei

#Função de cálculo das rotas ideais
#####Assumindo que a base de dados (nomeada Mapeamento.csv) será preparada por nossa equipe e seguirá o padrão de cada tupla conter: ponto mapeado de origem, ponto mapeado de destino, distancia em centímetros e a orientação desse percurso, nessa ordem.

######Além disso, utilizamos o Algoritmo de Dijkstra para o cálculo do caminho mais curto, ao transformar a base de dados em um grafo ponderado.

###### Para fins de teste e demonstração, utilizamos a planta da clínica disposta na pasta Plantas_teste e a base de dados Mapeamento.csv disposta nesse mesmo repositório.

##### Futuros ajustes serão feitos, como o cálculo da orientação e passagem para o bot no Telegram.

##### Para testar rotas entre outros pontos mapeados, basta alterar os termos entre aspas simples das variáveis *origem* e *destino* por algum ponto mapeado na linha imediatamente acima da atribuição às variáveis.
"""

#importando bibliotecas a serem utilizadas;
import pandas as pd
import numpy as np
import networkx as nx

#lendo o arquivo .cvs do mapeamento da clínica;
df = pd.read_csv('Mapeamento.csv', index_col=None)

#retornando um grafo do dataframe com lista de borda;
rota = nx.from_pandas_edgelist(df,source='Origem',target='Destino',edge_attr='Distancia')

#listando pontos mapeados;
rota.nodes()

#definindo origem e destino. Para diversos testes, basta alterar os termos entre aspas simples por algum dos pontos mapeados acima;
origem = 'recepcao1'
destino = 'e3'

#listando conexões mapeadas;
rota.edges()

#exibindo grafo do mapeamento completo;
nx.draw(rota,with_labels=True)

#utilizando a função do algoritmo de Dijkstra para o cálculo do caminho mais curto;
rota_ideal=nx.dijkstra_path(rota, source=origem, target=destino,weight=True)
rota_ideal

#fazendo da rota ideal(caminho mais curto) um subgrafo e exibindo-o;
rota_ideal_grafo = rota.subgraph(rota_ideal)
nx.draw(rota_ideal_grafo,with_labels=True)