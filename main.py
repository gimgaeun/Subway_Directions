# 프로그램 실행, 전체 흐름, 메뉴 관리
from data import Data
from graph import Graph
from path import Path
from ui import UI


class SubWayMain:
    def __init__(self):
        self.data = Data()
        self.graph = Graph()
        self.path = Path()
        self.ui = UI()
        self.csv_files = [
            "Daegu_SubwayLine1_Station.csv",
            "Daegu_SubwayLine2_Station.csv",
            "Daegu_SubwayLine3_Station.csv",
        ]

    def run(self, stations):
        while True:
            start_station_name = self.ui.input_start_station()
            if not start_station_name:
                self.ui.print_empty_input()
                continue

            end_station_name = self.ui.input_end_station()
            if not end_station_name:
                self.ui.print_empty_input()
                continue

            start_stations = self.data.find_stations(stations, start_station_name)
            end_stations = self.data.find_stations(stations, end_station_name)

            start_station_numbers = {station.number for station in start_stations}
            end_station_numbers = {station.number for station in end_stations}

            if not start_stations:
                self.ui.print_not_found_station()
                continue
            if not end_stations:
                self.ui.print_not_found_station()
                continue
            if start_station_numbers & end_station_numbers:
                self.ui.print_same_sation()
                continue
            if len(start_stations) > 1:
                start_stations = [self.ui.select_line(start_stations)]
            if len(end_stations) > 1:
                end_stations = [self.ui.select_line(end_stations)]

            routes = self.path.find_routes(self.graph, start_stations, end_stations)
            self.ui.print_routes(routes)
            break

    def main(self):
        # csv 파일 읽기
        stations = self.data.load_stations(self.csv_files)
        if not stations:
            print("프로그램을 실행할 수 없습니다.")
            return
        # 그래프 생성
        self.graph.build_graph(stations)
        # 메뉴
        while True:
            menu = self.ui.print_menu()
            if menu == "1":
                self.run(stations)
            elif menu == "2":
                self.ui.print_exit()
                break
            else:
                self.ui.print_invalid_menu()


if __name__ == "__main__":
    app = SubWayMain()
    app.main()
