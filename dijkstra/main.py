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
    nodes = []
    for link in links:
        if link["from"] not in [x["name"] for x in nodes]:
            nodes.append({
                "name":link["from"],
                "links":[link["to"]]
            })
        else:
            [x for x in nodes if x["name"] == link["from"]][0]["links"].append(link["to"])
    return nodes


def main(links):
    print(get_nodes_from_links(links))
    done_set = []
    not_done_set = []

    

main(links)
