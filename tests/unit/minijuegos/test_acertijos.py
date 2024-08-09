import unittest
from unittest.mock import patch, Mock
import src.minijuegos.acertijos as acertijos


class TestLoadAcertijos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sample_rid = {"acertijo1": ["respuesta1"],
                          "acertijo2": ["respuesta2"],
                          "acertijo3": ["respuesta3"]}

    def test_load_file(self):
        self.assertEqual(acertijos.load_riddles('tests/unit/minijuegos/test_riddles.json'), self.sample_rid)


class TestChooseAcertijos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sample_rid = {"acertijo1": ["respuesta1"],
                          "acertijo2": ["respuesta2"],
                          "acertijo3": ["respuesta3"]}

    def test_rid_choice_in(self):
        self.assertIn(acertijos.choose_riddle(self.sample_rid), self.sample_rid.items())


class TestPlayerGuessAcertijos(unittest.TestCase):

    @patch('src.minijuegos.acertijos.slow_print')
    @patch('src.minijuegos.acertijos.input')
    def test_low_magic(self, mock_input, mock_print):
        mock_player = Mock()
        mock_player.magic = 40
        acertijos.player_guess(mock_player, 'respuesta')
        mock_input.assert_not_called()
        mock_print.assert_called_once()
        self.assertEqual(mock_player.magic, 40)

    @patch('src.minijuegos.acertijos.slow_print')
    @patch('src.minijuegos.acertijos.input')
    def test_high_magic_reject(self, mock_input, mock_print):
        mock_player = Mock()
        mock_input.return_value = 'a'
        mock_player.magic = 51
        acertijos.player_guess(mock_player, 'respuesta')
        mock_input.assert_called_once()
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_player.magic, 51)

    @patch('src.minijuegos.acertijos.slow_print')
    @patch('src.minijuegos.acertijos.input')
    def test_high_magic_reject_second(self, mock_input, mock_print):
        mock_player = Mock()
        mock_input.side_effect = ['j', 'a']
        mock_player.magic = 51
        acertijos.player_guess(mock_player, 'respuesta')
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(mock_print.call_count, 2)
        self.assertEqual(mock_player.magic, 51)

    @patch('src.minijuegos.acertijos.slow_print')
    @patch('src.minijuegos.acertijos.input')
    def test_high_magic_accept_second(self, mock_input, mock_print):
        mock_player = Mock()
        mock_input.side_effect = ['j', 'b']
        mock_player.magic = 51
        acertijos.player_guess(mock_player, 'respuesta')
        mock_print.assert_any_call('respuesta')
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_player.magic, 1)


@patch('src.minijuegos.acertijos.choose_riddle', Mock(return_value=("acertijo1", ["respuesta1"])))
@patch('src.minijuegos.acertijos.player_guess', Mock())
@patch('src.minijuegos.acertijos.load_riddles', Mock())
@patch('src.minijuegos.acertijos.time.sleep', Mock())
@patch('src.minijuegos.acertijos.slow_print', Mock())
class TestPlayAcertijos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        def assert_not_called_with(self, *args, **kwargs):
            try:
                self.assert_called_with(*args, **kwargs)
            except AssertionError:
                return
            raise AssertionError(
                'Expected %s to not have been called.' % self._format_mock_call_signature(args, kwargs))

        Mock.assert_not_called_with = assert_not_called_with

    @patch('src.minijuegos.acertijos.slow_talk')
    @patch('src.minijuegos.acertijos.input')
    def test_tutorial_exit_third(self, mock_input, mock_talk):
        with patch('src.minijuegos.acertijos.slow_print') as mock_print:
            mock_player = Mock()
            mock_input.side_effect = ['fallo1', 'fallo2', 'salir']
            result = acertijos.play(mock_player, True)
            self.assertEqual(mock_input.call_count, 3)
            mock_print.assert_any_call("La respuesta era 'respuesta1'.")
            mock_talk.assert_any_call('-¡Incorrecto!')
            mock_talk.assert_not_called_with('-Tu respuesta es correcta.')
            self.assertIsNone(result)

    @patch('src.minijuegos.acertijos.slow_talk')
    @patch('src.minijuegos.acertijos.input')
    def test_tutorial_correct_second(self, mock_input, mock_talk):
        with patch('src.minijuegos.acertijos.slow_print') as mock_print:
            mock_player = Mock()
            mock_input.side_effect = ['fallo1', 'respuesta1', 'salir']
            result = acertijos.play(mock_player, True)
            self.assertEqual(mock_input.call_count, 2)
            mock_print.assert_not_called_with("La respuesta era 'respuesta1'.")
            mock_talk.assert_any_call('-¡Incorrecto!')
            mock_talk.assert_any_call('-Tu respuesta es correcta.')
            self.assertIsNone(result)

    @patch('src.minijuegos.acertijos.slow_talk')
    @patch('src.minijuegos.acertijos.input')
    def test_real_correct_second_deny_bet_third(self, mock_input, mock_talk):
        mock_player = Mock()
        mock_input.side_effect = ['no', '0', '2'] + ['intento1', 'respuesta1']
        result = acertijos.play(mock_player, False)
        self.assertEqual(mock_input.call_count, 5)
        mock_talk.assert_any_call('-Tu respuesta es correcta.')
        mock_talk.assert_any_call('-¡Incorrecto! Te queda sólo una oportunidad.')
        self.assertEqual(result, 1)

    @patch('src.minijuegos.acertijos.slow_talk')
    @patch('src.minijuegos.acertijos.input')
    def test_real_correct_first_accept_bet_first(self, mock_input, mock_talk):
        mock_player = Mock()
        mock_input.side_effect = ['1'] + ['respuesta1']
        result = acertijos.play(mock_player, False)
        mock_talk.assert_any_call('-Tu respuesta es correcta.')
        mock_player.sword_up.assert_called()
        mock_player.sword_down.assert_not_called()
        mock_player.receive_damage.assert_not_called()
        self.assertEqual(result, 1)

    @patch('src.minijuegos.acertijos.slow_talk')
    @patch('src.minijuegos.acertijos.input')
    def test_real_wrong_second_deny_bet_first(self, mock_input, mock_talk):
        mock_player = Mock()
        mock_input.side_effect = ['2'] + ['intento1', 'intento2', 'respuesta1']
        result = acertijos.play(mock_player, False)
        self.assertEqual(mock_input.call_count, 3)
        mock_talk.assert_not_called_with('-Tu respuesta es correcta.')
        mock_talk.assert_any_call('-¡Incorrecto! Te queda sólo una oportunidad.')
        mock_talk.assert_any_call('-No encontraste la respuesta al acertijo.')
        self.assertEqual(result, 0)

    @patch('src.minijuegos.acertijos.slow_talk')
    @patch('src.minijuegos.acertijos.input')
    def test_real_wrong_second_accept_bet_first_no_sword(self, mock_input, mock_talk):
        mock_player = Mock()
        mock_player.sword_lvl = None
        mock_player.health = 60
        mock_input.side_effect = ['1'] + ['error1', 'error2']
        result = acertijos.play(mock_player, False)
        mock_talk.assert_not_called_with('-Tu respuesta es correcta.')
        mock_player.sword_up.assert_not_called()
        mock_player.sword_down.assert_not_called()
        mock_player.receive_damage.assert_called()
        self.assertEqual(result, 0)

    @patch('src.minijuegos.acertijos.slow_talk')
    @patch('src.minijuegos.acertijos.input')
    def test_real_wrong_second_accept_bet_first_has_sword(self, mock_input, mock_talk):
        mock_player = Mock()
        mock_player.sword_lvl = 2
        mock_player.health = 60
        mock_input.side_effect = ['1'] + ['error1', 'error2']
        result = acertijos.play(mock_player, False)
        mock_talk.assert_not_called_with('-Tu respuesta es correcta.')
        mock_player.sword_up.assert_not_called()
        mock_player.sword_down.assert_called()
        mock_player.receive_damage.assert_not_called()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
