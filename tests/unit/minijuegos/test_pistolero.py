import unittest
from unittest.mock import patch, Mock
import src.minijuegos.pistolero as pistolero


@patch('src.minijuegos.pistolero.time.sleep', Mock())
class TestPlayerClassPistolero(unittest.TestCase):

    def setUp(self):
        self.player = pistolero.Player()

    def test_base_stats(self):
        self.assertEqual(self.player.bullets, 1)
        self.assertEqual(self.player.max_bullets, 5)
        self.assertEqual(self.player.hp, 2)
        self.assertEqual(self.player.opciones, {})

    def test_shoot(self):
        self.player.bullets = 2
        self.player.shoot()
        self.assertEqual(self.player.bullets, 1)

    def test_recharge(self):
        self.player.bullets = 2
        self.player.recharge()
        self.assertEqual(self.player.bullets, 3)

    def test_move_options_all(self):
        expected = {1: 'Me cubro', 2: 'Disparo', 3: 'Recargo'}
        self.player.bullets = 2
        self.player.get_move_options()
        self.assertEqual(self.player.opciones, expected)

    def test_move_options_no_bullets(self):
        expected = {1: 'Me cubro', 2: 'Recargo'}
        self.player.bullets = 0
        self.player.get_move_options()
        self.assertEqual(self.player.opciones, expected)

    def test_move_options_full_bullets(self):
        expected = {1: 'Me cubro', 2: 'Disparo'}
        self.player.bullets = 5
        self.player.get_move_options()
        self.assertEqual(self.player.opciones, expected)

    @patch('src.minijuegos.pistolero.print')
    @patch('src.minijuegos.pistolero.input')
    def test_player_choose(self, mock_input, mock_print):
        self.player.get_move_options = Mock()
        self.player.opciones = {1: 'Me cubro', 4: 'Disparo'}
        mock_input.side_effect = ['s', '2', '4', '1']
        result = self.player.player_choose_move()
        mock_print.assert_any_call('1) Me cubro')
        mock_print.assert_any_call('4) Disparo')
        self.assertEqual(mock_print.call_count, 9)
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(result, 4)

    def test_cpu_choose(self):
        self.player.get_move_options = Mock()
        self.player.opciones = {1: 'Me cubro', 4: 'Disparo'}
        result = self.player.cpu_choose_move()
        self.assertIn(result, [1,4])


if __name__ == '__main__':
    unittest.main()
