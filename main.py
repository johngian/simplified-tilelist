from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Tile:
    z: int
    x: int
    y: int

    def children(self):
        """Calculate the children tiles of a tile"""
        return [
            Tile(self.z + 1, self.x * 2, self.y * 2),
            Tile(self.z + 1, self.x * 2 + 1, self.y * 2),
            Tile(self.z + 1, self.x * 2, self.y * 2 + 1),
            Tile(self.z + 1, self.x * 2 + 1, self.y * 2 + 1),
        ]


class TileSet:
    def __init__(self, tilelistPath, maxzoom):
        self.tilelistPath = tilelistPath
        self.tileset = set()
        self.maxzoom = maxzoom

    @staticmethod
    def parse(entry):
        """Parse tile list entries"""
        entry = entry.rstrip()
        (z, x, y) = map(int, entry.split("/"))
        return Tile(z, x, y)

    def add(self, tile):
        """Add tile in tileset"""
        self.tileset.add(tile)

        if tile.z == self.maxzoom:
            return

        for child in tile.children():
            self.add(child)

    def read(self):
        """Read tilelist as input"""
        with open(self.tilelistPath, "r") as f:
            for line in f.readlines():
                tile = self.parse(line)
                self.add(tile)
