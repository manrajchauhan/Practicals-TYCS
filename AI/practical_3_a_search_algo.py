# -*- coding: utf-8 -*-
"""Practical 3 A* Search ALGO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13gs8kVVmjuwl21r1ps3W1qWQ6vucrLze
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

def astar_search(graph, start, goal):
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, (heuristic[start], start, 0, [start]))

    while open_list:
        _, current_node, current_cost, path = heapq.heappop(open_list)

        if current_node == goal:
            return path, current_cost

        closed_list.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor not in closed_list:
                new_cost = current_cost + cost
                new_path = path + [neighbor]
                f_value = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_value, neighbor, new_cost, new_path))

    return None, None

path, cost = astar_search(romania_map, 'Arad', 'Bucharest')
if path:
    print("Path:", path)
    print("Cost:", cost)
else:
    print("No path found.")

