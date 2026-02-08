from dataclasses import dataclass

@dataclass
class PointData:
    x: int
    y: int

p1 = PointData(3, 5)
print(p1)

p2 = PointData(3, 5)
print(p1 == p2)
