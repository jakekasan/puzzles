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
            nodes[link["from"]] = [link["to"]]
        else:
            nodes[link["from"]].append(link["to"])
    return nodes


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

    while end not in map(lambda x: x["node"],done_set):
        # sort not_done_set
        not_done_set = sort_set(not_done_set)


main(links,"a","g")

def sort_set(my_set):
    if my_set == []:
        return []
    pivot = my_set.pop(0)
    return filter(lambda x: my_set["dist"] < pivot["dist"],my_set) + [pivot] + filter(lambda x: my_set["dist"] >= pivot["dist"],my_set)
