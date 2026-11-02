# 경로 탐색, 방문 정보 관리
from route import Route


class PathFind:
    def find_routes(self, graph, start_stations, end_stations):
        routes = []
        for start_station in start_stations:
            for end_station in end_stations:
                visited = []
                path = []
                self.dfs(
                    graph,
                    start_station.number,
                    end_station.number,
                    visited,
                    path,
                    routes,
                )
        return routes

    def dfs(self, graph, current_station, end_station, visited, path, routes):
        visited.append(current_station)
        path.append(graph.stations[current_station])
        if current_station == end_station:
            route = Route(path.copy())
            routes.append(route)
        else:
            neighbors = graph.get_neighbors(current_station)
            for next_station in neighbors:
                if next_station not in visited:
                    self.dfs(graph, next_station, end_station, visited, path, routes)
        path.pop()
        visited.remove(current_station)
