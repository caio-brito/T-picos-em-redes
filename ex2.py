import networkx as nx
import matplotlib.pylab as plt
import numpy as np

n = 3000  
p = 0.01  

# Abrir grafo já gerado para não perder parâmetros no exercicio gerando novas arestas
#G = nx.read_gml("/home/brito/Documentos/desenvolvimento/Tópicos em redes/Exercicio 2/grafo_aleatorio.gml")
# Gerar o grafo Erdős–Rényi
G = nx.gnp_random_graph(n, p)



# Salvar o grafo gerado em formato GML
nx.write_gml(G, 'grafo_aleatorioN.gml')
print("Grafo salvo como 'grafo_aleatorio.gml'")

# Carregar o grafo salvo
G_loaded = nx.read_gml('grafo_aleatorioN.gml')

# Exibir algumas informações sobre o grafo
print(nx.info(G_loaded))

# Ajustar o tamanho do gráfico para uma visualização grande
plt.figure(figsize=(12, 12))

# Desenhar o grafo com um layout de força (force-directed layout)
pos = nx.spring_layout(G, seed=42)  # usar spring layout para uma distribuição mais espaçada
nx.draw(G, pos, node_size=10, node_color="black", edge_color="lightgray", with_labels=False, alpha=0.7)

# Exibir o gráfico
plt.title("Grafo Erdős–Rényi G(n, p) com n=3000 e p=0.001")
#plt.show()

# Pega os grais com networkx e faz a media do vetor retornado com o numpy
average_degree_networkx = np.mean([G.degree(n) for n in G.nodes()])

print(average_degree_networkx)

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