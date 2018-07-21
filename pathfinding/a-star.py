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
                    "node":node_count ,
                    "x": x,
                    "y": y,
                    "links": []
                })
                node_count += 1

    for node in nodes:
        for other_node in nodes:
            if node["node"] == other_node["node"]:
                continue
            if get_dist(node,other_node) < 10:
                if random.random() < 0.25:
                    new_link = {
                        "from":node["node"],
                        "to":other_node["node"],
                        "dist":get_dist(node,other_node)
                    }
                    links.append(new_link)
                    node["links"].append(new_link)
            

def get_nodes_from_links(links):
    nodes = {}
    nodes_geo
    for link in links:
        if link["from"] not in nodes:
            nodes[link["from"]] = {
                "x":,
                "y":,
                "links":[{
                    "node":link["to"],
                    "dist":link["dist"]
            }]}
        else:
            nodes[link["from"]]["links"].append({
                "node":link["to"],
                "dist":link["dist"]
            })
    return nodes


def a_star(start,end,links,nodes=None):
    # if nodes == None:
    #     nodes = get_nodes_from_links(links)
    
    


    done_set = []
    not_done_set = [{
        "node":start,
        "cost":0,
        "path":[]
    }]

    # end not in map(lambda x: x["node"],not_done_set)
    while len(not_done_set) > 0:
        # sort not_done_set
        not_done_set = sort_set(not_done_set)

        current_set = not_done_set.pop(0)

        if current_set["node"] in nodes.keys():
            for link in nodes[current_set["node"]]:
                not_done_set.append({
                    "node":link["node"],
                    "cost":(current_set["dist"]-get_dist())+link["dist"],
                    "path":current_set["path"]+[current_set["node"]]
                })

        done_set.append(current_set)

    print(done_set)