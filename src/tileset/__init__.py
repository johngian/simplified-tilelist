from math import floor
from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Tile:
    z: int
    x: int
    y: int

    @property
    def children(self):
        """Calculate the children tiles of a tile"""
        return [
            Tile(self.z + 1, self.x * 2, self.y * 2),
            Tile(self.z + 1, self.x * 2 + 1, self.y * 2),
            Tile(self.z + 1, self.x * 2, self.y * 2 + 1),
            Tile(self.z + 1, self.x * 2 + 1, self.y * 2 + 1),
        ]

    @property
    def parent(self):
        """Calculate the parent tile of a tile"""
        return Tile(self.z - 1, floor(self.x / 2), floor(self.y / 2))


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

    def addParent(self, tile):
        """Add parent tile in the tileset"""
        if tile.z < 0 or tile in self.tileset:
            return

        self.tileset.add(tile)
        self.addParent(tile.parent)

    def addChildren(self, tiles):
        """Add children tiles in the tileset"""
        for tile in tiles:
            if tile.z > self.maxzoom or tile in self.tileset:
                return

            self.tileset.add(tile)
            self.addChildren(tile.children)

    def read(self):
        """Read tilelist as input"""
        with open(self.tilelistPath, "r") as f:
            for line in f.readlines():
                tile = self.parse(line)
                self.addParent(tile.parent)
                self.addChildren(tile.children)
                self.tileset.add(tile)
