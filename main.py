from skystrain_astar import skystrain_astar
from load_data import load_data


# 1.get the path and distance from start_station to goal_station
astar = skystrain_astar()
path,distance = astar.get_path_distance('Columbia','Scott Road')
print(path)
print(distance)

# 2.get the distance between all stations and write into a file
station_list, _, _ = load_data().lines()
with open('stations_distance.csv', 'w') as file:
    # station name
    file.write(","+','.join(station_list)+"\n")
    for start_station in station_list:
        distances = []
        for end_station in station_list:
            path, distance = astar.get_path_distance(start_station, end_station)
            distances.append(str(distance))
        file.write(start_station+"," + ','.join(distances) + "\n")


