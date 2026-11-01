# 사용자 입력, 메뉴 출력, 결과 출력
def print_menu():
    print()
    print("지하철 길찾기")
    print("1. 길찾기")
    print("2. 종료")

    return input("메뉴를 선택하세요 : ").strip()


def input_start_station():
    return input("출발역을 입력하세요 : ").strip()


def input_end_station():
    return input("도착역을 입력하세요 : ").strip()


def print_route(route, route_number):
    print()
    print(f"[경로 {route_number}]")

    for i, station in enumerate(route.station_order):
        if i > 0:
            print("->", end="")
        print(f"{station.name}({station.line})", end="")
    print()
    print(f"역 수 : {route.get_station_count()}")
    print(f"환승 횟수 : {route.get_transfer_count()}")
    print(f"소요 시간 : {route.get_time()}분")


def print_routes(routes):
    print("검색 결과")

    if not routes:
        print("경로를 찾을 수 없습니다.")
        return

    for i, route in enumerate(routes, start=1):
        print_route(route, i)


def print_not_found_station():
    print()
    print("입력한 역을 찾을 수 없습니다.")
    print("다시 입력해주세요.")


def print_same_sation():
    print()
    print("출발역과 도착역은 다른 역이어야 합니다.")


def print_invalid_menu():
    print()
    print("잘못된 메뉴를 입력했습니다.")
    print("1 또는 2를 입력해주세요.")


def print_empty_input():
    print()
    print("역명을 비우지말고 입력해주세요.")


def print_exit():
    print()
    print("프로그램을 종료합니다.")
