#!/usr/bin/env python3

from __future__ import annotations

import sys
from typing import List, Union


class Node:
    __instances = {}

    def __init__(self, identifier: str):
        self.id = identifier

    @staticmethod
    def get_or_create(identifier: str) -> Node:
        if identifier in Node.__instances:
            instance = Node.__instances[identifier]
        else:
            instance = Node(identifier)
            Node.__instances[identifier] = instance
        return instance

    def __str__(self):
        return self.id


class Edge:
    def __init__(self, *ends: Node):
        self.ends = ends

    def __str__(self):
        return "->".join(map(str, self.ends))


class Graph:
    def __init__(self, *edges: Edge):
        self.edges = edges

    def __str__(self):
        string_data = []
        queue = ["start"]
        for name in queue:
            nodes = [
                edge[1] for edge in self.get_edges_matching(start=name)
            ]
            string_data.append("\t".join(nodes))
            queue.extend(nodes)
        return "\n".join(string_data)

    def get_edges_matching(
        self,
        start: Union[Node, None] = None,
        end: Union[Node, None] = None
    ) -> List[Edge]:
        matches = []
        for edge in self.edges:
            start_matches = (start and edge.ends[0] == start) or not start
            end_matches = (end and edge.ends[1] == end) or not end
            if start_matches and end_matches:
                matches.append(edge)
        return matches

    def get_edges_containing(self, node: Node) -> List[Edge]:
        return [edge for edge in self.edges if node in edge.ends]

    def find_all_paths(self) -> List[List[Edge]]:
        paths = []
        path_stack = [
            [edge] for edge in self.get_edges_matching(
                Node.get_or_create("start")
            )
        ]
        while path_stack:
            path = path_stack.pop()
            last_edge = path[-1]
            last_node = last_edge.ends[1]
            if last_node.id == "end":
                paths.append(path)
            else:
                """
                next_edges = [
                    edge for edge in self.get_edges_matching(last_node)
                    if edge not in path
                ]
                """
                next_edges = []
                for edge in self.get_edges_matching(last_node):
                    target_id = edge.ends[1].id
                    target_node = Node.get_or_create(target_id)
                    is_upper = target_id.isupper()
                    node_travel_count = sum([
                        1
                        for edge in path
                        if target_node == edge.ends[1]
                    ])
                    small_travel_target_hist = [
                        e.ends[1].id for e in path if e.ends[1].id.islower()
                    ]
                    double_traveled = len(list(set(small_travel_target_hist)))\
                        != len(small_travel_target_hist)
                    maximum_travels = 1 if double_traveled else 2
                    not_start_edge = target_id != "start"
                    if (is_upper or node_travel_count < maximum_travels) and \
                            not_start_edge:
                        next_edges.append(edge)
                path_stack.extend([[*path, nn] for nn in next_edges])

        return paths


def read_data(filepath: str) -> Graph:
    with open(filepath, "r") as f:
        lines = f.read().splitlines()

    edges = []
    for line in lines:
        points = line.split("-")
        ends = [Node.get_or_create(point) for point in points]
        edge = Edge(*ends)
        edges.append(edge)
        if points[0] != "start" and points[1] != "end":
            edges.append(Edge(*reversed(ends)))
    return Graph(*edges)


def main():
    graph = read_data(sys.argv[1])
    paths = graph.find_all_paths()
    print(f"There are {len(paths)} paths")
    for path in paths:
        print(",".join(list(map(lambda edge: edge.ends[0].id, path))) + ",end")


if __name__ == "__main__":
    main()
