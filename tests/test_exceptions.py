import unittest

from exelltech_remote_control.exceptions import CommunicationError, ExelltechError


class TestExceptions(unittest.TestCase):
    def test_communication_error_is_an_exelltech_error(self):
        self.assertTrue(issubclass(CommunicationError, ExelltechError))

    def test_exelltech_error_is_an_exception(self):
        self.assertTrue(issubclass(ExelltechError, Exception))


if __name__ == "__main__":
    unittest.main()
