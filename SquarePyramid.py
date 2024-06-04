import math


class SquarePyramid:
    def __init__(self, bottom_side, height):
        self.bottom_side = bottom_side if bottom_side > 0 else 0
        self.height = height if height > 0 else 0

    def get_bottom_side(self):
        return self.bottom_side

    def get_height(self):
        return self.height

    def get_bottom_area(self):
        return round((self.bottom_side**2), 2)

    def get_slant(self):
        return round(math.sqrt(self.height**2 + (self.bottom_side**2)/4), 2)
    
    def get_slant_total_area(self):
        return round(self.bottom_side * math.sqrt(self.bottom_side**2 + ((self.height**2)*4)), 2)


    def get_volume(self):
        volume = round((self.bottom_side**2)/3 * self.height, 2)
        return volume
