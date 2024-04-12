#!/usr/bin/env python3

# Dijkstra's algorithm

import heapq
from load_data import load_data

class skytrain_dijkstra:
    def __init__(self):
        self.__data = load_data()
        self.__station_list, self.__station_matrix, self.__station_distance = self.__data.lines()

    def get_path_distance(self, starting_station, target_station):
        graph = self.__station_distance

        distances = {station: float('inf') for station in graph}
        distances[starting_station] = 0

        parents = {station: None for station in graph}
        heap = [(0, starting_station)]

        while heap:
            current_distance, current_station = heapq.heappop(heap)
            if current_station == target_station:
                break

            if current_distance > distances[current_station]:
                continue

            for neighbor, weight in graph[current_station].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parents[neighbor] = current_station  # update the neighbor's parent
                    heapq.heappush(heap, (distance, neighbor))

        path = []
        current_station = target_station
        while current_station is not None:
            path.append(current_station)
            current_station = parents[current_station]

        path.reverse()
        return path, distances[target_station]
