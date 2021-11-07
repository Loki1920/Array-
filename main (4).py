# n, number of element as input
n = int(input("enter the number of input: "))

fromArr = []
toArr = []

for i in range(n // 2):
    ele1 = int(input("element for fromArr:"))

    fromArr.append(ele1)

for j in range(n // 2):
    ele2 = int(input("element for toArr:"))

    toArr.append(ele2)

print('fromArr is :', fromArr)
print("toArr is :", toArr)

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_edge(fromArr[0], toArr[0])
g.add_edge(fromArr[1], toArr[1])
g.add_edge(fromArr[2], toArr[2])
g.add_edge(fromArr[3], toArr[3])
g.add_edge(fromArr[4], toArr[4])

nx.draw_planar(g, with_labels=True)
plt.savefig("graph.png")

#counting number of links
