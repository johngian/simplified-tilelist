from unittest import TestCase, mock

from tileset import Tile, TileSet


class TestTile(TestCase):
    def test_tile_equal(self):
        self.assertEqual(Tile(1, 2, 3), Tile(1, 2, 3))

    def test_tile_not_equal(self):
        self.assertNotEqual(Tile(1, 2, 3), Tile(4, 5, 6))

    def test_tile_hashable(self):
        t1 = Tile(1,2,3)
        t2 = Tile(1,2,3)
        self.assertEqual(hash(t1), hash(t2))

class TestTileSet(TestCase):
    @mock.patch("tileset.TileSet.add")
    def test_tileset_read(self, mock_add):
        test_input = ["15/5/5", "15/12/12"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 15)
            tileset.read()

        call_list = [mock.call(Tile(15, 5, 5)), mock.call(Tile(15, 12, 12))]
        mock_add.assert_has_calls(call_list)

    def test_parse_entry(self):
        entry = "4/15/100"
        parsed = TileSet.parse(entry)
        self.assertEqual(parsed, Tile(4, 15, 100))

    def test_parse_entry_trailing_newline(self):
        entry = "4/15/100\n"
        parsed = TileSet.parse(entry)
        self.assertEqual(parsed, Tile(4, 15, 100))

    def test_tileset_add_single(self):
        test_input = ["0/0/0"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 1)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 5)

    def test_tileset_add_multiple(self):
        test_input = ["0/0/0", "0/1/1"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 1)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 10)

    def test_tileset_add_multiple_overlapping(self):
        test_input = ["0/0/0", "1/0/0"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 1)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 5)
