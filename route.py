# 역 수, 환승 횟수, 소요 시간 계산


class Route:
    def __init__(self, station_order):
        self.station_order = station_order

    def get_station_count(self):
        station_count = 0
        for i, station in enumerate(self.station_order):
            # 첫 번째 역
            if i == 0:
                station_count += 1
                continue
            # 이전역
            previous_station = self.station_order[i - 1]
            # 환승역인 경우 실제 역수에서 제외
            if (
                station.name == previous_station.name
                and station.line != previous_station.line
            ):
                continue
            station_count += 1
        return station_count

    def get_transfer_count(self):
        transfer_count = 0
        for i in range(len(self.station_order) - 1):
            current_station = self.station_order[i]
            next_station = self.station_order[i + 1]
            if current_station.line != next_station.line:
                transfer_count += 1
        return transfer_count

    def get_move_count(self):
        move_count = 0
        for i in range(len(self.station_order) - 1):
            current_station = self.station_order[i]
            next_station = self.station_order[i + 1]
            if (
                current_station.name == next_station.name
                and current_station.line != next_station.line
            ):
                continue
            move_count += 1
        return move_count

    def get_time(self):
        move_count = self.get_move_count()
        transfer_count = self.get_transfer_count()
        return move_count * 2 + transfer_count * 8
