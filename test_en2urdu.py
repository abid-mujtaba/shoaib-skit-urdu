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
        self.f = self.t.mu2e


    def test_non_urdu_characters(self):

        f = self.f
        self.assertEqual(f('{'), '{')
        self.assertEqual(f('['), '[')
        self.assertEqual(f('\\'), '\\')


    def test_urdu_characters_lowercase(self):

        f = self.f
        self.assertEqual(f('ا'), 'a')
        self.assertEqual(f('پ'), 'p')
        self.assertEqual(f('گ'), 'g')


    def test_urdu_characters_uppercase(self):

        f = self.f
        self.assertEqual(f('آ'), 'A')
        self.assertEqual(f('ٹ'), 'T')
        self.assertEqual(f('ں'), 'N')



class TestUrduMacros(unittest.TestCase):
    """
    Test translation of lines involving urdu macros ('dialog' and 'idialog')
    """

    def setUp(self):
        """
        Create a Translate object for testing
        """
        self.t = en2urdu.Translate()
        self.f = self.t.e2u_substr


    def test_urdu_macro_without_optional(self):
        """
        Test a line containing an urdu macro WITHOUT an optional argument (in square brackets)
        """

        f = self.f
        self.assertEqual(f('\dialog{xeib}{Adab}'), '\dialog{شعیب}{آداب}')


    def test_urdu_macro_with_options(self):
        """
        Test a line containing an urdu macro WITH an optional argument (in square brackets)
        """

        f = self.f
        self.assertEqual(f('\dialog[3.5em]{xeib}{Adab}'), '\dialog[3.5em]{شعیب}{آداب}')



if __name__ == '__main__':

    unittest.main()
