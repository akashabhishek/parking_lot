#!/usr/bin/env python3
import os
import sys

from parking_lot import ParkingLot


class ParkingLotMain:

    def __init__(self):
        self.parking_lot = ParkingLot()

    def process_file_input(self, file_path):
        if not os.path.exists(file_path):
            print("File not found")
            return
        with open(file_path, 'r') as file_data:
            for row in file_data:
                row = row.strip("\n")
                self.execute_command(_input=row)

    def process_command_line_input(self):
        try:
            while 1:
                _input = input()
                if _input == 'exit':
                    break
                self.execute_command(_input=_input)
        except Exception as e:
            print(e)
            print("Some error occurred")

    def execute_command(self, _input):
        command, *args = _input.split(" ")
        if hasattr(self.parking_lot, command):
            command_function = getattr(self.parking_lot, command)
            command_function(*args)
        else:
            print("Not Found")


if __name__ == '__main__':
    args = sys.argv
    parking_lot_obj = ParkingLotMain()
    if len(args) == 1:
        parking_lot_obj.process_command_line_input()
    elif len(args) == 2:
        parking_lot_obj.process_file_input(file_path=args[1])
    else:
        print("Invalid")
