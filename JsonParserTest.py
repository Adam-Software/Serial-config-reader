import unittest

from servo_config_reader.JsonParser import JsonParser


class JsonParserTest(unittest.TestCase):

    def testParseConfig(self):
        motors = JsonParser._ParseConfig('examples_config/position_range.json')
        print(motors[1].joint.id)

        self.assertEqual(motors[1].joint.id, 2)

    def testGetParam(self):
        motors = JsonParser.GetParam('examples_config/position_range.json')
        print(motors['Head'].joint.lover_limit)

        self.assertEqual(motors['Head'].joint.lover_limit, 1800)


if __name__ == '__main__':
    unittest.main()
