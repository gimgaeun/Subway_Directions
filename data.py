# CSV 데이터 읽기, 역 정보 관리
import csv


class Station:
    def __init__(self, number, name, line, transfer):
        # 역번호
        self.number = number
        # 역명
        self.name = name
        # 선명
        self.line = line
        # 환승역 여부
        self.transfer = transfer


def load_stations(filesname):
    stations = {}

    for filename in filesname:
        try:
            with open(filename, "r", encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)

                columns = ["역번호", "역명", "선명", "환승역여부"]

                if reader.fieldnames is None:
                    print(f"CSV 파일이 없습니다. : {filename}")
                    return {}

                for column in columns:
                    if column not in reader.fieldnames:
                        print(f"CSV 파일 '{filename}'에 '{column}'이 없습니다.")
                        return {}

                for row in reader:
                    number = int(row["역번호"])
                    name = row["역명"].strip()
                    line = row["선명"].strip()
                    transfer = row["환승역여부"].strip()

                    if not number or not name or not line:
                        continue

                    station = Station(number, name, line, transfer)

                    stations[number] = station
        except FileNotFoundError:
            print(f"CSV 파일을 찾을 수 없습니다. : {filename}")
            return {}

        except UnicodeDecodeError:
            print(f"CSV 파일의 인코딩을 읽을 수 없습니다. : {filename}")
            return {}

        except KeyError:
            print(f"CSV 파일의 데이터 형식이 올바르지 않습니다. : {filename}")
            return {}
    return stations


def find_stations(staions, name):
    result = []
    name = name.strip()

    for station in staions.values():
        if station.name == name:
            result.append(station)
            continue
    return result
