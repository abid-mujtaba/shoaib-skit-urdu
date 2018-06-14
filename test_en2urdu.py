import en2urdu
import unittest


class Testu2e(unittest.TestCase):
    """
    Test conversion from Urdu characters to English
    """

    def setUp(self):
        """
        Create a Translate object for testing
        """
        self.t = en2urdu.Translate()


    def test_non_urdu_characters(self):

        f = self.t.mu2e

        self.assertEqual(f('{'), '{')
        self.assertEqual(f('['), '[')
        self.assertEqual(f('\\'), '\\')


    def test_urdu_characters_lowercase(self):

        f = self.t.mu2e

        self.assertEqual(f('ا'), 'a')
        self.assertEqual(f('پ'), 'p')
        self.assertEqual(f('گ'), 'g')


    def test_urdu_characters_uppercase(self):

        f = self.t.mu2e

        self.assertEqual(f('آ'), 'A')
        self.assertEqual(f('ٹ'), 'T')
        self.assertEqual(f('ں'), 'N')



if __name__ == '__main__':

    unittest.main()
