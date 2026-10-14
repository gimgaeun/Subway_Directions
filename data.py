# CSV 데이터 읽기, 역 정보 관리
import csv


class Station:
    def __init__(self, number, name, line):
        self.number = number
        self.name = name
        self.line = line
