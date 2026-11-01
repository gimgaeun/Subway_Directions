# 경로 탐색, 방문 정보 관리
from route import Route


def find_routes(graph, start_stations, end_stations):
    routes = []
    for start_sation in start_stations:
        for end_station in end_stations:
            visited = set()
            current_path = []
            dfs(
                graph,
                start_sation.number,
                end_station.number,
                visited,
                current_path,
                routes,
            )
    return routes


def dfs(graph, current_number, end_number, visited, current_path, routes):
    visited.add(current_number)
    current_path.append(graph.stations[current_number])
    if current_number == end_number:
        route = Route(current_path.copy())
        routes.append(route)
    else:
        neighbors = graph.get_neighbors(current_number)
        for next_number in neighbors:
            if next_number not in visited:
                dfs(graph, next_number, end_number, visited, current_path, routes)
    current_path.pop()
    visited.remove(current_number)
