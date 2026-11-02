# 지하철 역 연결 관계 구성 및 관리
from itertools import combinations


class Graph:
    def __init__(self):
        # 지하철 역 정보 저장
        self.stations = {}
        # 각 역과 연결된 인접 역 정보 저장
        self.connections = {}

    # 역 정보 추가
    def add_station(self, station):
        if station.number not in self.stations:
            self.stations[station.number] = station
            self.connections[station.number] = []

    # 인접 역 정보 추가
    def add_connection(self, station1, station2):
        self.add_station(station1)
        self.add_station(station2)
        num1, num2 = station1.number, station2.number
        if num1 not in self.connections[num2]:
            self.connections[num2].append(num1)
        if num2 not in self.connections[num1]:
            self.connections[num1].append(num2)

    def get_neighbors(self, station_number):
        return self.connections.get(station_number, [])

    def build_graph(self, stations):

        # 모든 역 추가
        for station in stations.values():
            self.add_station(station)

        # 노선별 분류
        lines = {}
        for station in stations.values():
            if station.line not in lines:
                lines[station.line] = []
            lines[station.line].append(station)

        # 환승역 필터링 후 이름별 분류
        transfer_stations = {}
        for station in stations.values():
            if station.transfer == "Y":
                if station.name not in transfer_stations:
                    transfer_stations[station.name] = []
                transfer_stations[station.name].append(station)

        # 같은 노선 인접 역 연결
        for line_stations in lines.values():
            line_stations.sort(key=lambda station: int(station.number))

            for i in range(len(line_stations) - 1):
                current_station = line_stations[i]
                next_station = line_stations[i + 1]
                self.add_connection(current_station, next_station)

        # 환승역 연결
        for samename_stations in transfer_stations.values():
            if len(samename_stations) > 1:
                for station1, station2 in combinations(samename_stations, 2):
                    if station1.line != station2.line:
                        self.add_connection(station1, station2)
