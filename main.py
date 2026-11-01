# 프로그램 실행, 전체 흐름, 메뉴 관리
from data import load_stations, find_stations
from graph import build_graph
from path import find_routes
import ui

csv_files = [
    "Daegu_SubwayLine1_Station.csv",
    "Daegu_SubwayLine2_Station.csv",
    "Daegu_SubwayLine3_Station.csv",
]


def run(stations, graph):
    while True:
        start_station_name = ui.input_start_station()
        if not start_station_name:
            ui.print_empty_input()
            continue
        end_station_name = ui.input_end_station()
        if not end_station_name:
            ui.print_empty_input()
            continue
        start_stations = find_stations(stations, start_station_name)
        end_stations = find_stations(stations, end_station_name)

        start_station_numbers = {station.number for station in start_stations}
        end_station_numbers = {station.number for station in end_stations}

        if not start_stations:
            ui.print_not_found_station()
            continue
        if not end_stations:
            ui.print_not_found_station()
            continue
        if start_station_numbers & end_station_numbers:
            ui.print_same_sation()
            continue
        routes = find_routes(graph, start_stations, end_stations)
        ui.print_routes(routes)
        break


def main():
    # csv 파일 읽기
    stations = load_stations(csv_files)
    if not stations:
        print("프로그램을 실행할 수 없습니다.")
        return
    # 그래프 생성
    graph = build_graph(stations)
    # 메뉴
    while True:
        menu = ui.print_menu()
        if menu == "1":
            run(stations, graph)
        elif menu == "2":
            ui.print_exit()
            break
        else:
            ui.print_invalid_menu()


if __name__ == "__main__":
    main()
