import unittest
import src.utils.functions as functions
from unittest.mock import patch, call


@patch('src.utils.functions.sys.stdout.write')
@patch('src.utils.functions.sys.stdout.flush')
@patch('src.utils.functions.time.sleep')
class TestFunctions(unittest.TestCase):

    def test_slow_print(self, mock_sleep, mock_flush, mock_write):
        result = functions.slow_print("Test")
        calls_expected = [call("T"), call("e"), call("s"), call("t"), call("\n")]
        mock_write.asset_has_calls(calls_expected)
        mock_sleep.assert_any_call(0.02)
        mock_sleep.assert_called_with(1)
        self.assertEqual(mock_flush.call_count, 5)
        self.assertIsNone(result)

    def test_slow_talk(self, mock_sleep, mock_flush, mock_write):
        result = functions.slow_talk("Test")
        calls_expected = [call("T"), call("e"), call("s"), call("t"), call("\n")]
        mock_write.asset_has_calls(calls_expected)
        mock_sleep.assert_any_call(0.08)
        mock_sleep.assert_called_with(1)
        self.assertEqual(mock_flush.call_count, 5)
        self.assertIsNone(result)

    def test_scream(self, mock_sleep, mock_flush, mock_write):
        result = functions.scream("Test")
        calls_expected = [call("T"), call("E"), call("S"), call("T"), call("\n")]
        mock_write.asset_has_calls(calls_expected)
        mock_sleep.assert_any_call(0.4)
        mock_sleep.assert_called_with(1)
        self.assertEqual(mock_flush.call_count, 5)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
