import unittest
from allocine.allocine import Allocine


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.allocine = Allocine()

    def test_person(self):
        actor = self.allocine.person("194788")

        self.assertEqual(actor["person"]["birthDate"], "1988-11-06")

if __name__ == "__main__":
    unittest.main()