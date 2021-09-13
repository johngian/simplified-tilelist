from unittest import TestCase, mock

from tileset import Tile, TileSet


class TestTile(TestCase):
    def test_tile_equal(self):
        self.assertEqual(Tile(1, 2, 3), Tile(1, 2, 3))

    def test_tile_not_equal(self):
        self.assertNotEqual(Tile(1, 2, 3), Tile(4, 5, 6))

    def test_tile_hashable(self):
        t1 = Tile(1, 2, 3)
        t2 = Tile(1, 2, 3)
        self.assertEqual(hash(t1), hash(t2))


class TestTileSet(TestCase):
    @mock.patch("tileset.TileSet.addChildren")
    @mock.patch("tileset.TileSet.addParent")
    def test_tileset_read(self, mock_addParent, mock_addChildren):
        test_input = ["15/5/5", "15/12/12"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 15)
            tileset.read()

        parent_list = [mock.call(Tile(14, 2, 2)), mock.call(Tile(14, 6, 6))]
        mock_addParent.assert_has_calls(parent_list)
        children_list = [
            mock.call(
                [
                    Tile(z=16, x=10, y=10),
                    Tile(z=16, x=11, y=10),
                    Tile(z=16, x=10, y=11),
                    Tile(z=16, x=11, y=11),
                ]
            ),
            mock.call(
                [
                    Tile(z=16, x=24, y=24),
                    Tile(z=16, x=25, y=24),
                    Tile(z=16, x=24, y=25),
                    Tile(z=16, x=25, y=25),
                ]
            ),
        ]
        mock_addChildren.assert_has_calls(children_list)

    def test_parse_entry(self):
        entry = "4/15/100"
        parsed = TileSet.parse(entry)
        self.assertEqual(parsed, Tile(4, 15, 100))

    def test_parse_entry_trailing_newline(self):
        entry = "4/15/100\n"
        parsed = TileSet.parse(entry)
        self.assertEqual(parsed, Tile(4, 15, 100))

    def test_tileset_add_single_minzoom(self):
        test_input = ["0/0/0"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 1)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 5)

    def test_tileset_add_multiple_minzoom(self):
        test_input = ["0/0/0", "0/1/1"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 1)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 10)

    def test_tileset_add_multiple_overlapping_minzoom(self):
        test_input = ["0/0/0", "1/0/0"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 1)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 5)

    def test_tileset_add_single_z_between_maxzoom(self):
        test_input = ["2/0/0"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 3)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 7)

    def test_tileset_add_multiple_z_between_maxzoom(self):
        test_input = ["2/0/0", "2/10/10"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 3)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 14)

    def test_tileset_add_multiple_overlapping_z_between_maxzoom(self):
        test_input = ["2/0/0", "3/0/0"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 3)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 7)

    def test_tileset_add_single_maxzoom(self):
        test_input = ["3/0/0"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 3)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 4)

    def test_tileset_add_multiple_maxzoom(self):
        test_input = ["3/0/0", "3/10/10"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 3)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 8)

    def test_tileset_add_multiple_overlapping_maxzoom(self):
        test_input = ["3/0/0", "3/1/1"]
        test_input_file = "\n".join(test_input)

        mock_open = mock.mock_open(read_data=test_input_file)
        with mock.patch("builtins.open", mock_open):
            tileset = TileSet("/path/to/tilelist", 0, 3)
            tileset.read()
        self.assertEqual(len(tileset.tileset), 5)
