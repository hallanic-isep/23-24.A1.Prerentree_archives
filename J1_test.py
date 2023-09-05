import unittest

import juste_prix

class Tests(unittest.TestCase):

    def test_bravo(self):
        self.assertEqual(juste_prix.verif(5,5), True)

if __name__ == '__main__':
    unittest.main()
