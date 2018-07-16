#!/usr/bin/env python3

links = [
    {
        "from":"a",
        "to":"b",
        "dist":2
    },
    {
        "from":"a",
        "to":"c",
        "dist":7
    },
    {
        "from":"a",
        "to":"d",
        "dist":4
    },
    {
        "from":"b",
        "to":"c",
        "dist":4
    },
    {
        "from":"d",
        "to":"e",
        "dist":3
    },
    {
        "from":"d",
        "to":"f",
        "dist":4
    },
    {
        "from":"f",
        "to":"g",
        "dist":2
    },
    {
        "from":"e",
        "to":"g",
        "dist":3
    },
    {
        "from":"c",
        "to":"g",
        "dist":20
    },
]

def get_nodes_from_links(links):
    nodes = {}
    for link in links:
        if link["from"] not in nodes:
            nodes[link["from"]] = [{
                "node":link["to"],
                "dist":link["dist"]
            }]
        else:
            nodes[link["from"]].append({
                "node":link["to"],
                "dist":link["dist"]
            })
    return nodes


def sort_set(my_set):
    if my_set == []:
        return []
    pivot = my_set.pop(0)
    return list(filter(lambda x: x["dist"] < pivot["dist"],my_set)) + [pivot] + list(filter(lambda x: x["dist"] >= pivot["dist"],my_set))



def main(links,start,end):
    nodes = (get_nodes_from_links(links))
    done_set = []
    not_done_set = [{
        "node":start,
        "dist":0,
        "path":[]
    }]
    lst = ["a","b","c"]
    print(lst)
    lst.pop(0)
    print(lst)

    # end not in map(lambda x: x["node"],not_done_set)
    while len(not_done_set) > 0:
        # sort not_done_set
        not_done_set = sort_set(not_done_set)

        current_set = not_done_set.pop(0)

        if current_set["node"] in nodes.keys():
            for link in nodes[current_set["node"]]:
                not_done_set.append({
                    "node":link["node"],
                    "dist":current_set["dist"]+link["dist"],
                    "path":current_set["path"]+[current_set["node"]]
                })

        done_set.append(current_set)

    print(done_set)




main(links,"a","g")

def get_distance(links,prev,current):
    for link in links:
        if link["from"] == prev and link["to"] == current:
            return link["dist"]
    return False
