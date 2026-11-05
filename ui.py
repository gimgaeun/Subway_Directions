# 사용자 입력, 메뉴 출력, 결과 출력
class UI:
    def print_menu(self):
        print()
        print("=" * 50)
        print("지하철 길찾기")
        print("=" * 50)
        print("1. 길찾기")
        print("2. 종료")

        return input("메뉴를 선택하세요 : ").strip()

    def input_start_station(self):
        print("-" * 50)
        return input("출발역을 입력하세요 : ").strip()

    def input_end_station(self):
        return input("도착역을 입력하세요 : ").strip()

    def print_route(self, route, route_number):
        print()
        print(f"[경로 {route_number}]")

        stations = []
        for station in route.station_order:
            stations.append(f"{station.name}({station.line})")
        print("->".join(stations))

        print()
        print(f"역 수 : {route.get_station_count()}")
        print(f"환승 횟수 : {route.get_transfer_count()}")
        print(f"소요 시간 : {route.get_time()}분")
        print("-" * 50)

    def print_routes(self, routes):
        print()
        print("=" * 50)
        print("검색 결과")
        print("=" * 50)

        if not routes:
            print("경로를 찾을 수 없습니다.")
            return

        for i, route in enumerate(routes):
            self.print_route(route, i + 1)

    def print_not_found_station(self):
        print()
        print("입력한 역을 찾을 수 없습니다.")
        print("다시 입력해주세요.")

    def print_same_station(self):
        print()
        print("출발역과 도착역은 다른 역이어야 합니다.")
        print("다시 입력해주세요.")

    def print_invalid_menu(self):
        print()
        print("잘못된 메뉴를 입력했습니다.")
        print("1 또는 2를 입력해주세요.")

    def print_empty_input(self):
        print()
        print("역명을 비우지말고 입력해주세요.")

    def print_exit(self):
        print()
        print("프로그램을 종료합니다.")

    def select_line(self, stations):
        print()
        print(f"{stations[0].name}은 환승역입니다.")

        for i, station in enumerate(stations):
            print(f"{i + 1}. {station.line}")

        while True:
            choice = input("노선을 선택하세요. : ").strip()
            if choice.isdigit():
                number = int(choice)

                if number > 0 and number <= len(stations):
                    return stations[number - 1]
            print("잘못된 입력입니다.")
            print("표시된 번호 중 하나를 선택해주세요.")
