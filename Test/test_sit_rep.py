from unittest.mock import patch
import unittest
import sit_rep


class TestSitRep(unittest.TestCase):

    # Tests no exception when sit_rep initialized in Client mode
    @patch('sit_rep.get_input', return_value='c')
    def test_main_client(self, input):
        self.assertIsNone(sit_rep.main())

    # Tests no exception when sit_rep initialized in Server mode
    @patch('sit_rep.get_input', return_value='s')
    def test_main_server(self, input):
        self.assertIsNone(sit_rep.main())

    # Expects Exception: [Exception] for an invalid input
    @patch('sit_rep.get_input', return_value='q')
    def test_main_invalid(self, input):
        with self.assertRaises(Exception) as context:
            sit_rep.main()

        self.assertTrue('Invalid Response. Enter c for Client or s for Server' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
