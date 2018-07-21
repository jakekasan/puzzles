# a-star

import random

names = []
for letter in range(97,97+26):
    names.append(chr(letter))

def get_dist(node1,node2):
    return ((node1["x"] - node2["x"])**2 + (node1["y"] - node2["y"])**2)**0.5

def make_nodes(nodes=None,max_x=100,max_y=100,number_of_nodes=100):
    if nodes == None:
        nodes = {}
        node_count = 0
    else:
        nodes = nodes
        node_count = max(list(nodes.keys())) + 1


    x_pos = [x for x in range(max_x) if x not in [a["x"] for a in nodes.values()]]
    y_pos = [y for y in range(max_y) if y not in [a["x"] for a in nodes.values()]]

    for x in x_pos:
        for y in y_pos:
            if random.random() < (number_of_nodes/(max_x*max_y)):
                nodes[node_count] = {
                    "node": node_count,
                    "x": x,
                    "y": y,
                    "links": []
                }
                node_count += 1
            if len(nodes) >= number_of_nodes:
                return nodes

    while len(nodes) < number_of_nodes:
        nodes = make_nodes(nodes=nodes,max_x=max_x,max_y=max_y,number_of_nodes=number_of_nodes-len(nodes))
    return nodes


def make_links(nodes):
    links = []
    for _,node in nodes.items():
        for _,other_node in nodes.items():
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
    return nodes,links


def make_network(max_x=100,max_y=100,number_of_nodes=100):
    
    nodes = make_nodes(nodes=None,max_x=max_x,max_y=max_y,number_of_nodes=number_of_nodes)
    nodes,links = make_links(nodes)


    return nodes,links


def a_star(start,end,nodes):

    print("Searching from {} to {}".format(start,end))
    print("Network:")
    print(nodes)

    done_set = []
    not_done_set = [{
        "node":start,
        "dist":0,
        "cost":0,
        "path":[]
    }]

    # end not in map(lambda x: x["node"],not_done_set)
    while end not in list(map(lambda x: x["node"],not_done_set)):
        # if not_done_set is empty
        if not_done_set == []:
            print("Cannot reach end in network")
            return
        # sort not_done_set
        not_done_set = sort_set(not_done_set)

        current_set = not_done_set.pop(0)

        if current_set["node"] in nodes.keys():
            for link in nodes[current_set["node"]]["links"]:
                not_done_set.append({
                    "node":link["to"],
                    "dist":current_set["dist"] + link["dist"],
                    "cost":get_dist(nodes[link["to"]],nodes[link["from"]]),
                    "path":current_set["path"]+[current_set["node"]]
                })

        done_set.append(current_set)

    print("Finished")
    print(done_set)
    print(not_done_set)

def sort_set(my_set):
    if my_set == []:
        return []
    pivot = my_set.pop(0)
    return list(filter(lambda x: (x["cost"]+x["dist"]) < (pivot["cost"]+pivot["dist"]),my_set)) + [pivot] + list(filter(lambda x: (x["cost"]+x["dist"]) >= (pivot["cost"]+pivot["dist"]),my_set))


def main():
    nodes,links = make_network(max_x=100,max_y=100,number_of_nodes=200)

    a_star(1,max(list(nodes.keys())),nodes)


main()