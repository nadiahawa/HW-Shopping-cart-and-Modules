class Sqrft:
    def __init__(self, width, length):
        self.width = width
        self.length = length 
    def area(self):
        self.width = int(input('Please enter width: '))
        self.length = int(input('Please enter length: '))
        self.area = self.width*self.length
        print(f'The square footage of this property is: {self.area}. Very nice!')

my_house = Sqrft(4,3)
my_house.area()

def sqrft(length,width):
    return length * width
