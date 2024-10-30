class Logic:
    def __init__(self):
        self.pi = 3.1415926
        self.r = 42
        self.S = self.pi * self.r ** 2
    
    def calculate_area(self):
        return self.S
    
    def check_distance(self, point):
        distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
        return distance <= self.r

