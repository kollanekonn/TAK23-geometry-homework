from SquarePyramid import SquarePyramid


class Model:
    def __init__(self):
        pass

    @staticmethod
    def is_number(user_input):
        try:
            num = int(user_input)
            if num > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def get_user_input(self, bottom_side, height):
        if self.is_number(bottom_side) and self.is_number(height):
            bottom_side = int(bottom_side)
            height = int(height)
            square_pyramid = SquarePyramid(bottom_side, height)
            bottom_side = square_pyramid.get_bottom_side()
            bottom_area = square_pyramid.get_bottom_area()
            slant = square_pyramid.get_slant()
            slant_total_area = square_pyramid.get_slant_total_area()
            volume = square_pyramid.get_volume()
            return (f''
                    f'Põhiserv: {bottom_side} \n'
                    f'Kõrgus: {height} \n'
                    f'Apoteem {slant}\n'
                    f'Põhja pindala {bottom_area} \n'
                    f'Külgede pindala {slant_total_area} \n'
                    f'Ruumala {volume}'
                    )
        else:
            return False
