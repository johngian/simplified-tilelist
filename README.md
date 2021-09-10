# Deduped map tilelist

Given an input file with a list of line seperated tiles in `{zoom}/{x}/{y}` format, generate a distinct list of map tiles for all zoom levels up to `maxzoom`.

## Usage

```
usage: cli.py [-h] tilelist_path maxzoom

Given a tile list as input, generate a distinct list of map tiles consisted of all the parent and children tiles recursively up to a zoom level.

positional arguments:
  tilelist_path  Path to the tilelist input file.
  maxzoom        The maxzoom of the generated tilelist.

optional arguments:
  -h, --help     show this help message and exit
```

## Context

This CLI tool is built as a way to generate a deduplicated tile list of distinct tiles based on the `imposm3` expired tile output. The reason behind this is to deduplicate tiles and optimize tile pregeneration by avoiding generating the same tile multiple times.

## Dependencies

- Python >= 3.7
