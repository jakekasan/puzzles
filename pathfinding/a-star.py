# a-star

import random

names = []
for letter in range(97,97+26):
    names.append(chr(letter))

def get_dist(node1,node2):
    return ((node1["x"] - node2["x"])**2 + (node1["y"] - node2["y"])**2)**0.5

def make_network(x=100,y=100,number_of_nodes=100)
    nodes = []
    links = []
    node_count = 0

    for x in range(100):
        for y in range(100):
            if random.random() < (100/(x*y)):
                nodes.append({
                    "id":node_count ,
                    "x": x,
                    "y": y,
                    "links": []
                })
                node_count += 1

    for node in nodes:
        for other_node in nodes:
            if node["id"] == other_node["id"]:
                continue
            if get_dist(node,other_node) < 10:
                if random.random() < 0.25:
                    new_link = {
                        "from":node["id"],
                        "to":other_node["id"],
                        "dist":get_dist(node,other_node)
                    }
                    links.append(new_link)
                    node["links"].append(new_link)
            

def 


def a_star(start,end,links):
