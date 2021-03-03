class Table:
    def __init__(self):
        self._length = 0
        self._width = 0
        self._height = 0
    @property
    def length(self):
        return self._length
    @length.setter
    def length(self, length):
        if length in range(100, 300):
            self._length = length
        else:
            print('Wrong length')
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        if width in range(50, 250):
            self._width = width
        else:
            print('Wrong width')

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        if height in range(20, 150):
            self._height = height
        else:
            print('Wrong height')

    def table_area(self):
        return self.length*self._width


my_table = Table()

my_table.length = 250
my_table.width = 120
my_table.height = 80

print(f'Table area {my_table.table_area()} cm2')
