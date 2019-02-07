import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from spec.parking_lot import ParkingLot


class TestParkingLot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parking_lot = ParkingLot()
        cls.number_of_slots = 1
        cls.registration_no = "KA-01-HH-1234"
        cls.color = "White"

    def test_0_create_parking_lot(self):
        parking_slots = 6
        self.parking_lot.create_parking_lot(parking_slots)
        self.assertEqual(len(self.parking_lot.slots), parking_slots, msg="Error while creating parking lot")

    def test_1_park(self):
        self.parking_lot.park(self.registration_no, self.color)
        for i in self.parking_lot.slots.values():
            if not i.is_available and i.car:
                self.assertEqual(i.car.registration_no, self.registration_no, "Error in parking the car")
                self.assertEqual(i.car.color, self.color, "Error in parking the car")

    def test_2_leave(self):
        self.parking_lot.leave(self.number_of_slots)
        self.assertTrue(self.parking_lot.slots[self.number_of_slots].is_available, "Some Error Occurred")

    @classmethod
    def tearDownClass(cls):
        del cls.parking_lot


if __name__ == '__main__':
    unittest.main()
