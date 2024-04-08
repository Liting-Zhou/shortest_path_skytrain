# load and parse stations data
class load_data:
    def __init__(self):
        self.__lon_lat = './data/station_coordinates.txt'
        self.__line = './data/station_lines.txt'

    # get the coordinates of stations
    def coordinates(self):
        station_location = {}
        for line in open(self.__lon_lat):
            part = line.strip().split("\t")
            lon = float(part[0])
            lat = float(part[1])
            station_name = part[-1]
            if station_name not in station_location:
                station_location[station_name] = [lat,lon]
        return station_location

    # get the distance between stations
    def lines(self):
        station_list = []
        station_distance = {}
        for line in open(self.__line):
            part = line.strip().split("\t")
            distance = float(part[1])
            station1 = part[2]
            station2 = part[3]
            if station1 not in station_list:
                station_list.append(station1)
            if station2 not in station_list:
                station_list.append(station2)
            if station1 not in station_distance:
                station_distance[station1] = {station2:distance}
            else:
                station_distance[station1][station2] = distance
            if station2 not in station_distance:
                station_distance[station2] = {station1: distance}
            else:
                station_distance[station2][station1] = distance
        station_matrix = [[0 for _ in range(len(station_list))] for _ in range(len(station_list))]
        for index,station in enumerate(station_list):
            if station in station_distance:
                for k,v in station_distance[station].items():
                    other_station_index = station_list.index(k)
                    station_matrix[index][other_station_index] = station_matrix[other_station_index][index] = v
        return station_list,station_matrix,station_distance










