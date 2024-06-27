from math import hypot
def distance(p_1, p_2):
    return hypot(p_1[0]-p_2[0], p_1[1]-p_2[1])
def perimeter(polygon):
    pairs = zip(polygon, polygon[1:]+polygon[:1])
    return sum(
        distance(p1, p2) for p1, p2 in pairs
    )