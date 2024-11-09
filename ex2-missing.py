import networkx as nx
import matplotlib.pylab as plt
import numpy as np

# Carregando o grafo a partir do arquivo GML
G = nx.read_gml("/home/brito/Documentos/desenvolvimento/Tópicos em redes/Exercicio 2/GraphMissingEdges.gml")

# Calculando os graus dos nós
degrees = [G.degree(n) for n in G.nodes()]

# Calculando a distribuição de graus
degree_count = np.bincount(degrees)
x = np.arange(len(degree_count))
y = degree_count / sum(degree_count)  # Normalizando para que a soma seja 1

# Plotando a distribuição de graus
plt.figure(figsize=(10, 6))
plt.bar(x, y, width=0.8, color='b', alpha=0.7)
plt.xlabel('Grau dos nós')
plt.ylabel('Frequência relativa')
plt.title('Distribuição de Graus do Grafo')
plt.xticks(x)  # Adiciona os valores do grau como ticks no eixo x
plt.grid(axis='y')
plt.show()
