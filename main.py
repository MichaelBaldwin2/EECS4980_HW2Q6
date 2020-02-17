# https://xkcd.com/353/

import networkx as nx
import matplotlib.pyplot as pl

# Load the Karate (pronounced Care-Ra-Tae) data
karateGraph = nx.read_gml('data/karate.gml')

# Calculate the degree, eigenvector, closeness, and betweenness centrality for each node
degCen = nx.degree_centrality(karateGraph)
eigCen = nx.eigenvector_centrality(karateGraph)
clsCen = nx.closeness_centrality(karateGraph)
betCen = nx.betweenness_centrality(karateGraph)

# Print it all to console
print('Degree centrality per node:')
for i in degCen:
    print(i, ':', degCen[i])
print('\nEigenvector centrality per node:')
for i in eigCen:
    print(i, ':', eigCen[i])
print('\nCloseness centrality per node:')
for i in clsCen:
    print(i, ':', clsCen[i])
print('\nBetweenness centrality per node:')
for i in betCen:
    print(i, ':', betCen[i])
