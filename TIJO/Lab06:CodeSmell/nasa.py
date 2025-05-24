import unittest

class Vehicle:
    def __init__(self, x=0, y=0, direction="N"):
        self.x = x
        self.y = y
        self.direction = direction
        self.start_x = x
        self.start_y = y

    def move_forward(self, steps=1):
        if self.direction == "N":
            self.y += steps
        elif self.direction == "S":
            self.y -= steps
        elif self.direction == "E":
            self.x += steps
        elif self.direction == "W":
            self.x -= steps

    def move_back(self, steps=1):
        self.move_forward(-steps)

    def move_left(self):
        self.direction = {"N": "W", "W": "S", "S": "E", "E": "N"}[self.direction]

    def move_right(self):
        self.direction = {"N": "E", "E": "S", "S": "W", "W": "N"}[self.direction]

    def get_position(self):
        return self.x, self.y

    def get_start_point(self):
        return self.start_x, self.start_y

    def get_direction(self):
        return self.direction


class VehicleTest(unittest.TestCase):
    def test_initial_position(self):
        vehicle = Vehicle()
        self.assertEqual(vehicle.get_position(), (0, 0))
        self.assertEqual(vehicle.get_start_point(), (0, 0))
        self.assertEqual(vehicle.get_direction(), "N")

    def test_move_forward(self):
        vehicle = Vehicle()
        vehicle.move_forward(3)
        self.assertEqual(vehicle.get_position(), (0, 3))

    def test_move_backwards(self):
        vehicle = Vehicle()
        vehicle.move_back(2)
        self.assertEqual(vehicle.get_position(), (0, -2))

    def test_move_left(self):
        vehicle = Vehicle()
        vehicle.move_left()
        self.assertEqual(vehicle.get_direction(), "W")

    def test_move_right(self):
        vehicle = Vehicle()
        vehicle.move_right()
        self.assertEqual(vehicle.get_direction(), "E")


if __name__ == "__main__":
    unittest.main()
