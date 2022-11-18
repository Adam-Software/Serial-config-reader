import unittest

from serial_config_reader.JsonParser import JsonParser


class JsonParserTest(unittest.TestCase):

    def test_something(self):
        motors = JsonParser.ParseConfig('examples_config/position_range.json')
        print(motors)


if __name__ == '__main__':
    unittest.main()
