class Rectangle:
    width = int()
    height = int()

    def __init__(self, width, height):
        if width & height is str():
            width_parts = width.split('=')
            self.width = int(width_parts[1])

            height_parts = height.split('=')
            self.height = int(height_parts[1])

        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = int(width)
        return

    def set_height(self, height):
        self.height = int(height)
        return

    def get_area(self):
        area = (self.width * self.height)
        return area

    def get_perimeter(self):
        perimeter = (self.width * 2 + self.height * 2)
        return perimeter

    def get_diagonal(self):
        diagonal = int((self.width ** 2 + self.height ** 2) ** 0.5)
        return diagonal

    def get_picture(self):
        if self.height or self.width > 50:
            print('Too big for picture.')

        else:
            picture = str()
            for i in range(self.height):
                for t in range(self.width):
                    picture = picture + '*'
                picture = picture + '\n'

            return picture

    def get_amount_inside(self, obj):
        square = obj
        amount = int((self.width * self.height) / (square.get_area()))

        return amount


class Square(Rectangle):

    def __init__(self, width):
        if width is str():
            width_parts = width.split('=')
            self.width = int(width_parts[1])
        self.width = width
        self.height = width

    def set_side(self, side):
        self.width = side
        self.height = side


rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
