import unittest
from unittest.mock import patch, Mock
import src.minijuegos.acertijos as acertijos


class TestRiddles(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sample_rid = {"acertijo1": ["respuesta1"],
                          "acertijo2": ["respuesta2"],
                          "acertijo3": ["respuesta3"]}

    def test_load_file(self):
        self.assertEqual(acertijos.load_riddles('tests/unit/minijuegos/test_riddles.json'), self.sample_rid)

    def test_rid_choice(self):
        self.assertIn(acertijos.choose_riddle(self.sample_rid), self.sample_rid.items())


class TestPlayerGuess(unittest.TestCase):

    @patch('src.minijuegos.acertijos.slow_print')
    @patch('src.minijuegos.acertijos.input')
    def test_player_guess(self, mock_input, mock_print):
        mock_player = Mock()

        mock_player.magic = 40
        acertijos.player_guess(mock_player, 'respuesta')
        mock_input.asser_not_called()
        mock_print.assert_called_once()
        self.assertEqual(mock_player.magic, 40)

        mock_print.reset_mock()
        mock_input.reset_mock()
        mock_input.return_value = 'a'
        mock_player.magic = 51
        acertijos.player_guess(mock_player, 'respuesta')
        mock_input.assert_called_once()
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_player.magic, 51)

        mock_print.reset_mock()
        mock_input.reset_mock()
        mock_input.side_effect = ['j', 'a']
        mock_player.magic = 51
        acertijos.player_guess(mock_player, 'respuesta')
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_player.magic, 51)

        mock_print.reset_mock()
        mock_input.reset_mock()
        mock_input.side_effect = ['j', 'b']
        mock_player.magic = 51
        acertijos.player_guess(mock_player, 'respuesta')
        mock_print.assert_any_call('respuesta')
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_player.magic, 1)

if __name__ == '__main__':
    unittest.main()
