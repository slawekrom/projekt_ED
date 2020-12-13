

class SplitInfo:
    def __init__(self, split_point: float, column, count, lower: bool, o_class):
        self.split_point = split_point
        self.column = column
        self.count = count
        self.lower = lower
        self.objects_class = o_class