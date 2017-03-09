import unittest
from CartManager import retrieve_document

class TestTechnique(unittest.TestCase):

    def test_level1(self):
        document = retrieve_document("level1/data.json")
        print(document)

if __name__ == '__main__':
    unittest.main()