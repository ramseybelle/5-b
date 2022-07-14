class Taxicab:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.odometer = 0

    def move_x(self, value):
        self.x_coord += value
        self.odometer += abs(value)

    def move_y(self, value):
        self.y_coord += value
        self.odometer += abs(value)

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def get_odometer(self):
        return self.odometer


# Testing the function here. ignore/remove the code below if not required
cab = Taxicab(5, -8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odometer())
