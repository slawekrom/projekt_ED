

class Distance:
    def __init__(self, distance, index1, index2):
        self.distance = distance
        self.index1 = index1
        self.index2 = index2

    def __repr__(self) -> str:
        return f'index1= {self.index1}, index2= {self.index2}, distance= {self.distance}'
