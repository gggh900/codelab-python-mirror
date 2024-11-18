PRECISION = 9

def geohash(lat_lon: tuple[float,float]) -> str:
    return str(lat_lon)


print(type(geohash((1.55, 1.332))))
#print(type(geohash((1.55, '1.332'))))
