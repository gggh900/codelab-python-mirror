from typing import NamedTuple

PRECISION=9
class Coordinate(NamedTuple):
    lat: float
    lon: float

def geohash(lat_lon: Coordinate)->str:
    return str(lat_lon)

print(type(geohash(Coordinate(1.23, 4.43))))
