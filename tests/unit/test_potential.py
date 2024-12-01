import unittest
from sphinx_parser.potential import (
    get_potential_path,
    _is_vasp_potential,
    _remove_hash_tag,
)
import os


class TestStinx(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Get the path to the folder of this file
        d = os.path.dirname(os.path.realpath(__file__))
        cls.file_path = os.path.join(d, "..", "static")

    def test_path_exists(self):
        self.assertTrue(os.path.exists(get_potential_path("Ag")))

    def test_is_vasp_potential(self):
        with open(os.join(self.file_path, "potentials", "Ag_POTCAR"), "r") as f:
            file_content = f.read()
            file_content = _remove_hash_tag(file_content)
        self.assertTrue(_is_vasp_potential("Ag"))


if __name__ == "__main__":
    unittest.main()
