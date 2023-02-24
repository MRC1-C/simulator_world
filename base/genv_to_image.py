genv = " CNN - RNN + CNN + CNN - CNN"

def analysis_genv(genv):
    genv = genv.split(" ")[1:]
    gens = []
    modes = []
    for i in range(len(genv)):
        if i%2 ==0:
            gens.append(genv[i])
        else: 
            modes.append(genv[i])
    return modes, gens

import networkx as nx
import matplotlib.pyplot as plt


def draw_grapt(genv):
    G = nx.DiGraph()
    mode, gen = analysis_genv(genv)
    def get_color(node):
        if node == "CNN":
            return "blue"
        if node == "RNN":
            return 'red'
        if node == "-":
            return 'gray'
        if node == "X":
            return "purple"
        if node == "AUTOENCODER":
            return 'yellow'
        if node == "S":
            return "pink"
        if node == "F":
            return "black"


    colormap = [get_color("S"),get_color(gen[0])]
    G.add_node(0)
    G.add_node(1)
    G.add_edge(0,1)
    n_node = 1
    for i in range(len(mode)):
        if mode[i] == "+":
            G.add_nodes_from([
                (n_node+1),
                (n_node+2),
                (n_node+3)
                ])
            colormap = colormap + [get_color(gen[i+1]),get_color("S"),get_color('-')]
            G.add_edge(n_node,n_node+3)
            G.add_edge(n_node+1,n_node+3)
            G.add_edge(n_node+2,n_node+1)
            n_node +=3
        if mode[i] == "-":
            G.add_node(n_node+1)
            colormap = colormap + [get_color(gen[i+1])]
            G.add_edge(n_node,n_node+1)
            n_node+=1
    G.add_node(n_node+1)
    G.add_edge(n_node,n_node+1)
    colormap.append(get_color("F"))
    nx.draw_circular(G, with_labels=False,node_color=colormap)
    plt.draw()
    plt.savefig('genv_to_image.png')

draw_grapt(genv)