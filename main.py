from skystrain_astar import skystrain_astar
from skytrain_dijkstra import skytrain_dijkstra
from load_data import load_data
from fare import fare


# 1.get the path and distance from start_station to goal_station
astar = skystrain_astar()
path, distance = astar.get_path_distance('Columbia','Scott Road')
print("A*:", path, distance)

dijkstra = skytrain_dijkstra()
path, distance = dijkstra.get_path_distance('Columbia','Scott Road')
print("Dijkstra:", path, distance)

# # 2.get the distance between all stations and write into a file
# station_list, _, _ = load_data().lines()
# with open('stations_distance.csv', 'w') as file:
#     # station name
#     file.write(","+','.join(station_list)+"\n")
#     for start_station in station_list:
#         distances = []
#         for end_station in station_list:
#             path, distance = astar.get_path_distance(start_station, end_station)
#             distances.append(str(distance))
#         file.write(start_station+"," + ','.join(distances) + "\n")

# 3.get the distance and fare between all stations and write into a file
station_list, _, _ = load_data().lines()
with open('stations_distance_fare.csv', 'w') as file:
    # station name
    file.write(","+','.join(station_list)+"\n")
    for start_station in station_list:
        distances_and_fares = []
        for end_station in station_list:
            path, distance = astar.get_path_distance(start_station, end_station)
            distance_km = distance / 1000
            fare_cost = fare(distance_km)
            distances_and_fares.append(f"{distance_km:.2f}km - ${fare_cost:.2f}")
        file.write(start_station+"," + ','.join(distances_and_fares) + "\n")
