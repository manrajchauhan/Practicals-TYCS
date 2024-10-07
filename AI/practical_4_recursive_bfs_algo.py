# -*- coding: utf-8 -*-
"""Practical 4 Recursive BFS ALGO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vPOAy3MrIYudpGVHHFUuFHvvUTSAHDZq
"""

from collections import deque
import heapq

romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75 },
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97 },
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138 , 'Bucharest': 101 },
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85 },
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

heuristic = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea':193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

def rbfs(graph, start, goal, f_limit):
    def expand_node(node, f_limit):
        if node == goal:
            return [node], 0, True

        successors = []
        for neighbor, cost in graph[node].items():
            g = cost
            h = heuristic[neighbor]
            f = g + h
            successors.append((f, neighbor, g))

        if not successors:
            return None, float('inf'), False

        successors.sort()

        best_f = successors[0][0]
        best_node = successors[0][1]

        if best_f > f_limit:
            return None, best_f, False

        alternative_f = float('inf')
        if len(successors) > 1:
            alternative_f = successors[1][0]

        result, best_f, success = expand_node(best_node, min(f_limit, alternative_f))

        if success:
            return [node] + result, best_f, True

        return None, best_f, False

    result, _, _ = expand_node(start, f_limit)
    return result


result = rbfs(romania_map, 'Arad', 'Bucharest', float('inf'))

if result:
    print("Path found (RBFS):", result)
else:
    print("No path found (RBFS).")