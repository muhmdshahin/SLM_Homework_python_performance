import time
import pandas as pd
import networkx

edge = pd.read_csv("musae_git_edges.csv")
target = pd.read_csv("musae_git_target.csv")

graph = networkx.Graph()
graph.add_nodes_from(target["id"])
for index, row in edge.iterrows():
    graph.add_edge(row["id_1"], row["id_2"])


edges_df = pd.read_csv("musae_git_edges.csv")
classes_df = pd.read_csv("musae_git_target.csv")


graph = networkx.Graph()
graph.add_nodes_from(classes_df["id"])
for index, row in edges_df.iterrows():
    graph.add_edge(row["id_1"],row["id_2"])


start = time.time()
deg_ml = [0]*len(classes_df)
deg_web = [0]*len(classes_df)
ml_target = classes_df["ml_target"].tolist()

for edge in graph.edges():
    edge_src, edge_dst = edge[0], edge[1]
    if ml_target[edge_dst] == 1:
        deg_ml[edge_src] = 1
    else:
        deg_web[edge_src] = 1

    if ml_target[edge_src] == 1:
        deg_ml[edge_dst] = 1
    else:
        deg_web[edge_dst] = 1

print("Execution Time in seconds: %s "%(time.time()-start))