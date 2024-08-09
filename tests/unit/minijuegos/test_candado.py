import unittest
from unittest.mock import patch, Mock
import src.minijuegos.candado as candado


class TestAskCandado(unittest.TestCase):

    @patch('src.minijuegos.candado.slow_print')
    @patch('src.minijuegos.candado.input')
    def test_ask_player_sixth(self, mock_input, mock_print):
        mock_input.side_effect = ['', 'ab', '110', '102d', '10002', '0000']
        result = candado.ask_player()
        self.assertEqual(mock_input.call_count, 6)
        self.assertEqual(mock_print.call_count, 6)
        self.assertEqual(result, '0000')


@patch('src.minijuegos.candado.time.sleep', Mock())
class TestCompareCandado(unittest.TestCase):

    @patch('src.minijuegos.candado.slow_print')
    def test_all_wrong(self, mock_print):
        guess = '1234'
        real = '0000'
        candado.compare(guess, real)
        mock_print.assert_called_once_with("Todos los números son incorrectos.")

    @patch('src.minijuegos.candado.slow_print')
    def test_wrong_position(self, mock_print):
        guess = '1234'
        real = '0121'
        candado.compare(guess, real)
        mock_print.assert_called_once_with("2 números son correctos pero están en la posición equivocada.")

        mock_print.reset_mock()
        guess = '0121'
        real = '1999'
        candado.compare(guess, real)
        mock_print.assert_called_once_with("1 números son correctos pero están en la posición equivocada.")

    @patch('src.minijuegos.candado.slow_print')
    def test_right_position(self, mock_print):
        guess = '1234'
        real = '1894'
        candado.compare(guess, real)
        mock_print.assert_called_once_with("2 números son correctos y están en el lugar correcto.")

        mock_print.reset_mock()
        guess = '1234'
        real = '1100'
        candado.compare(guess, real)
        mock_print.assert_called_once_with("1 números son correctos y están en el lugar correcto.")

    @patch('src.minijuegos.candado.slow_print')
    def test_right_wrong_position(self, mock_print):
        guess = '1934'
        real = '1894'
        candado.compare(guess, real)
        mock_print.assert_called_once_with("2 números son correctos y están en el lugar correcto,"
                                           " 1 números son correctos pero están en la posición equivocada.")

        mock_print.reset_mock()
        guess = '1231'
        real = '1100'
        candado.compare(guess, real)
        mock_print.assert_called_once_with("1 números son correctos y están en el lugar correcto,"
                                           " 1 números son correctos pero están en la posición equivocada.")


@patch('src.minijuegos.candado.random.randint', Mock(return_value=345))
@patch('src.minijuegos.candado.time.sleep', Mock())
class TestPlayCandado(unittest.TestCase):

    @patch('src.minijuegos.candado.slow_print')
    @patch('src.minijuegos.candado.ask_player')
    def test_tutorial_success_third(self, mock_ask, mock_print):
        mock_player = Mock()
        mock_ask.side_effect = ['0213', '1124', '0345', '2291']
        result = candado.play(mock_player, True)
        self.assertEqual(mock_ask.call_count, 3)
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call('¡La clave introducida es correcta!')
        self.assertIsNone(result)

    @patch('src.minijuegos.candado.slow_print')
    @patch('src.minijuegos.candado.ask_player')
    def test_real_success_third(self, mock_ask, mock_print):
        mock_player = Mock()
        mock_ask.side_effect = ['0213', '1124', '0345', '2291']
        result = candado.play(mock_player, False)
        self.assertEqual(mock_ask.call_count, 3)
        self.assertEqual(mock_print.call_count, 7)
        mock_print.assert_any_call('El candado se abre y puedes cruzar.')
        mock_player.receive_damage.assert_called_with(0, 20)
        self.assertEqual(result, 1)

    @patch('src.minijuegos.candado.slow_print')
    @patch('src.minijuegos.candado.ask_player')
    def test_real_fail_low_magic(self, mock_ask, mock_print):
        mock_player = Mock()
        mock_player.magic = 10
        mock_ask.side_effect = ['0000' for _ in range(10)]
        result = candado.play(mock_player, False)
        self.assertEqual(mock_ask.call_count, 7)
        mock_print.assert_any_call("No lograste abrir el candado.")
        mock_player.receive_damage.assert_called_with(15, 0)
        self.assertEqual(result, 0)

    @patch('src.minijuegos.candado.slow_print')
    @patch('src.minijuegos.candado.ask_player')
    @patch('src.minijuegos.candado.input')
    def test_real_fail_high_magic_reject_second(self, mock_input, mock_ask, mock_print):
        mock_player = Mock()
        mock_player.magic = 30
        mock_ask.side_effect = ['0000' for _ in range(10)]
        mock_input.side_effect = ['a', '2']
        result = candado.play(mock_player, False)
        self.assertEqual(mock_ask.call_count, 7)
        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_any_call("No lograste abrir el candado.")
        mock_player.receive_damage.assert_called_with(15, 0)
        self.assertEqual(result, 0)

    @patch('src.minijuegos.candado.slow_print')
    @patch('src.minijuegos.candado.ask_player')
    @patch('src.minijuegos.candado.input')
    def test_real_fail_high_magic_accept_first_fail(self, mock_input, mock_ask, mock_print):
        mock_player = Mock()
        mock_player.magic = 30
        mock_ask.side_effect = ['0000' for _ in range(10)]
        mock_input.side_effect = ['1']
        result = candado.play(mock_player, False)
        self.assertEqual(mock_ask.call_count, 10)
        self.assertEqual(mock_input.call_count, 1)
        mock_print.assert_any_call("No lograste descifrar la combinación.")
        mock_player.receive_damage.assert_called_with(15, 0)
        self.assertEqual(mock_player.magic, 5)
        self.assertEqual(result, 0)

    @patch('src.minijuegos.candado.slow_print')
    @patch('src.minijuegos.candado.ask_player')
    @patch('src.minijuegos.candado.input')
    def test_real_fail_high_magic_accept_first_success(self, mock_input, mock_ask, mock_print):
        mock_player = Mock()
        mock_player.magic = 30
        mock_ask.side_effect = ['0000' for _ in range(8)] + ['0345']
        mock_input.side_effect = ['1']
        result = candado.play(mock_player, False)
        self.assertEqual(mock_ask.call_count, 9)
        self.assertEqual(mock_input.call_count, 1)
        mock_print.assert_any_call("El candado se abre y puedes cruzar.")
        mock_player.receive_damage.assert_not_called()
        self.assertEqual(mock_player.magic, 5)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
