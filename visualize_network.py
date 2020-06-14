import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json
from statistics import mean,median,variance,stdev

# jsonファイル読み込み
with open("correlation.json", "r", encoding="utf8") as f:
    correlation = json.load(f)

# グラフ作成
G = nx.Graph()
G.add_nodes_from(correlation.keys())
for owner, cor in correlation.items():
    for member, count in cor.items():
        if not G.has_edge(owner, member):
            G.add_edge(owner, member, weight=count)
        else:
            G.edges[owner,member]["weight"] += count

print(G.edges(data=True))

# 次数中心性に応じて頂点のサイズを決める
between_cent = nx.degree_centrality(G)
node_size = [1000 * size for size in list(between_cent.values())]

# 描画
plt.figure(figsize=(1000, 1000))
pos=nx.spring_layout(G, k=8)
nx.draw_networkx_nodes(G, pos, node_size=node_size)
nx.draw_networkx_labels(G, pos, fontsize=0.1, font_family="Yu Gothic")
width = np.array([d['weight'] for (u, v, d) in G.edges(data=True)])
mean_ = mean(width)

variance_ = 0
for w in width:
    variance_ += (mean_ - w)**2
variance_ = variance_/len(correlation.keys())

width_std = 50*(width-mean_)/variance_
nx.draw_networkx_edges(G, pos, width=width_std)
plt.show()