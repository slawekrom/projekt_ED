

class SplitInfo:
    def __init__(self, split_point: float, column, count, lower: bool):
        self.split_point = split_point
        self.column = column
        self.count = count
        self.lower = lower
