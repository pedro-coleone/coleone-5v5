
class StrategyGridControl:

    def __init__(self):
        strategy_grid = [[12.5, 107], [37.5, 107], [62.5, 107], [87.5, 107], [112.5, 107], [137.5, 107],
                         [12.5, 91], [37.5, 91], [62.5, 91], [87.5, 91], [112.5, 91], [137.5, 91],
                         [12.5, 65], [37.5, 65], [62.5, 65], [87.5, 65], [112.5, 65], [137.5, 65],
                         [12.5, 39], [37.5, 39], [62.5, 39], [87.5, 39], [112.5, 39], [137.5, 39]
                         [12.5, 13], [37.5, 13], [62.5, 13], [87.5, 13], [112.5, 13], [137.5, 13]]

    def calculate_distance_two_points(self, coordinate1, coordinate2):
        """Calculates the distance between two points"""
        return sqrt((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2)
    def calculate_grid_coordinate(self, body):
        """Calculates the grid coordinate of a body by returning the index of the closest point in the strategy grid"""
        body_coordinates = body.get_coordinates()
        body_coordinates = [body_coordinates.X, body_coordinates.Y]
        coordinate_index = 0
        current_distance = 9999999
        for index, coordinate in enumerate(strategy_grid):
            distance = self.calculate_distance_two_points(body_coordinates, coordinate)
            if distance < current_distance:
                current_distance = distance
                coordinate_index = index

        return coordinate_index



