class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):  # equal
        return self.lat == otro.lat and self.lon == otro.lon

    def __ne__(self, otro):  # not equal
        return self.lat != otro.lat or self.lon != otro.lon

    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(44, 27)
coords2 = Coordenadas(45, 27)
# coords2 = coords
# print(coords == coords2) True
print(coords == coords2)  # False
print(coords <= coords2)
