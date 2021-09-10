import argparse

from tileset import TileSet


def main():
    parser = argparse.ArgumentParser(
        description="Given a tile list as input, generate a distinct "
        "list of map tiles consisted of all the parent and children tiles "
        "recursively up to a zoom level."
    )
    parser.add_argument(
        "tilelist_path", help="Path to the tilelist input file.", type=str
    )
    parser.add_argument(
        "maxzoom", help="The maxzoom of the generated tilelist.", type=int
    )
    args = parser.parse_args()

    ts = TileSet(args.tilelist_path, args.maxzoom)
    ts.read()

    for tile in ts.tileset:
        print(f"{tile.z}/{tile.x}/{tile.y}")
