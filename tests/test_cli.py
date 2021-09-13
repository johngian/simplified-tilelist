from argparse import Namespace
from unittest import TestCase, mock

from tileset.cli import main


class CliTest(TestCase):
    @mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=Namespace(tilelist_path="/path/to/tilelist", minzoom=0, maxzoom=1),
    )
    def test_main(self, mock_parse_args):
        test_input = ["0/0/0", "1/0/0"]
        test_input_file = "\n".join(test_input)
        mock_open = mock.mock_open(read_data=test_input_file)

        with mock.patch("builtins.open", mock_open):
            with mock.patch("builtins.print") as mock_print:
                main()
                call_list = [
                    mock.call("1/0/1"),
                    mock.call("1/1/0"),
                    mock.call("0/0/0"),
                    mock.call("1/0/0"),
                    mock.call("1/1/1"),
                ]
                mock_print.assert_has_calls(call_list)
