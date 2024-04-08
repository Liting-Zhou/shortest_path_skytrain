import heapq
import math
from load_data import load_data


class skystrain_astar:
    def __init__(self):
        self.__data = load_data()
        self.__station_list, self.__station_matrix, self.__station_distance = self.__data.lines()
        self.__station_location = self.__data.coordinates()

    def __haversine(self, lat_lon1, lat_lon2):
        # Convert latitude and longitude from degrees to radians
        lat1 = math.radians(lat_lon1[0])
        lon1 = math.radians(lat_lon1[1])
        lat2 = math.radians(lat_lon2[0])
        lon2 = math.radians(lat_lon2[1])
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        # Radius of the Earth in kilometers
        distance = 6371 * c
        return distance

    def __heuristic(self, index1, index2, s_list, s_location):
        return self.__haversine(s_location[s_list[index1]], s_location[s_list[index2]])

    def __get_neighbors(self, s_matrix, current_station_index):
        neighbors = []
        for i, distance in enumerate(s_matrix[current_station_index]):
            if distance > 0:
                neighbors.append((i, distance))
        return neighbors

    def get_path_distance(self, start_station, goal_station):
        start_station_index = self.__station_list.index(start_station)
        goal_station_index = self.__station_list.index(goal_station)
        open_set = [(0, start_station_index)]  # Priority queue of (f_score, node)
        closed_set = set()
        came_from = {}  # For reconstructing the path

        g_score = {node: float('inf') for node in range(len(self.__station_matrix))}
        g_score[start_station_index] = 0

        while open_set:
            f_score, current_station_index = heapq.heappop(open_set)
            if current_station_index == goal_station_index:
                # Reconstruct the path
                path = []
                distance = 0
                while current_station_index in came_from:
                    path.append(self.__station_list[current_station_index])
                    current_station_index = came_from[current_station_index]
                path.append(self.__station_list[start_station_index])
                path.reverse()
                for index in range(len(path) - 1):
                    distance += self.__station_distance[path[index]][path[index + 1]]
                return path, distance

            closed_set.add(current_station_index)

            for neighbor, distance in self.__get_neighbors(self.__station_matrix, current_station_index):
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current_station_index] + distance
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_station_index
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.__heuristic(neighbor, goal_station_index, self.__station_list,
                                                                   self.__station_location)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None, float("inf")  # No path found
