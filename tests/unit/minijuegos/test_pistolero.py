import unittest
from unittest.mock import patch, call, Mock
import src.minijuegos.pistolero as pistolero


@patch('src.minijuegos.pistolero.time.sleep', Mock())
class TestPlayerClassPistolero(unittest.TestCase):

    def setUp(self):
        self.player = pistolero.Player()

    def test_base_stats(self):
        self.assertEqual(self.player.cpu_first_move, 0)
        self.assertTrue(self.player.start_game)
        self.assertTrue(self.player.start_round)
        self.assertEqual(self.player.bullets, 1)
        self.assertEqual(self.player.max_bullets, 5)
        self.assertEqual(self.player.hp, 2)
        self.assertEqual(self.player.opciones, {})

    def test_bullets_three_stats(self):
        self.player = pistolero.Player(3)
        self.assertEqual(self.player.cpu_first_move, 0)
        self.assertTrue(self.player.start_game)
        self.assertTrue(self.player.start_round)
        self.assertEqual(self.player.bullets, 1)
        self.assertEqual(self.player.max_bullets, 3)
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

    def test_cpu_choose_no_start_round(self):
        self.player.cpu_first_move = 1
        self.player.start_game = False
        self.player.start_round = False
        self.player.get_move_options = Mock()
        self.player.opciones = {1: 'Me cubro', 4: 'Disparo'}
        result = self.player.cpu_choose_move(1)
        self.assertIn(result, [1, 4])
        self.assertEqual(self.player.cpu_first_move, 1)
        self.assertFalse(self.player.start_game)
        self.assertFalse(self.player.start_round)

    def test_cpu_choose_start_round_start_game(self):
        self.player.cpu_first_move = 0
        self.player.start_game = True
        self.player.start_round = True
        self.player.get_move_options = Mock()
        self.player.opciones = {1: 'Me cubro', 4: 'Disparo'}
        result = self.player.cpu_choose_move(1)
        self.assertIn(result, [1, 4])
        self.assertNotEqual(self.player.cpu_first_move, 0)
        self.assertEqual(self.player.cpu_first_move, result)
        self.assertFalse(self.player.start_game)
        self.assertFalse(self.player.start_round)

    def test_cpu_choose_start_round_no_start_game_real(self):
        self.player.cpu_first_move = 1
        self.player.start_game = False
        self.player.start_round = True
        self.player.get_move_options = Mock()
        self.player.opciones = {1: 'Me cubro', 4: 'Disparo'}
        result = self.player.cpu_choose_move(0)
        self.assertIn(result, [2, 3])
        self.assertEqual(self.player.cpu_first_move, 1)
        self.assertFalse(self.player.start_game)
        self.assertFalse(self.player.start_round)

    def test_cpu_choose_start_round_no_start_game_tutorial(self):
        self.player.cpu_first_move = 1
        self.player.start_game = False
        self.player.start_round = True
        self.player.get_move_options = Mock()
        self.player.opciones = {1: 'Me cubro', 4: 'Disparo'}
        result = self.player.cpu_choose_move(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.player.cpu_first_move, 1)
        self.assertFalse(self.player.start_game)
        self.assertFalse(self.player.start_round)


@patch('src.minijuegos.pistolero.time.sleep', Mock())
@patch('src.minijuegos.pistolero.scream', Mock())
@patch('src.minijuegos.pistolero.slow_talk', Mock())
@patch('src.minijuegos.pistolero.slow_print')
@patch('src.minijuegos.pistolero.Player')
class TestPlayPistolero(unittest.TestCase):

    def setUp(self):
        self.mock_gen_player = Mock(gun_lvl=0)
        self.mock_in_player = Mock(name='player', hp=1, opciones={1: 'Me cubro', 2: 'Recargo', 3: 'Disparo'})
        self.mock_in_cpu = Mock(name='cpu', hp=1, opciones={1: 'Me cubro', 2: 'Recargo', 3: 'Disparo'})

    def test_loss(self, mock_Player_class, mock_print):
        self.mock_in_player.hp = 0
        mock_Player_class.side_effect = [self.mock_in_player, self.mock_in_cpu]
        result = pistolero.play(self.mock_gen_player, 0)
        mock_print.assert_called_once_with('Fuiste derrotado.')
        self.mock_gen_player.gun_down.assert_called_once()
        self.assertEqual(result, 0)

    def test_win(self, mock_Player_class, mock_print):
        self.mock_in_cpu.hp = 0
        mock_Player_class.side_effect = [self.mock_in_player, self.mock_in_cpu]
        result = pistolero.play(self.mock_gen_player, 0)
        mock_print.assert_called_once_with('Sales airoso de este enfrentamiento.')
        self.mock_gen_player.gun_up.assert_called_once()
        self.assertEqual(result, 1)

    def test_Rec_Dis(self, mock_Player_class, mock_print):
        self.mock_in_player.player_choose_move.return_value = 2
        self.mock_in_cpu.cpu_choose_move.return_value = 3
        mock_Player_class.side_effect = [self.mock_in_player, self.mock_in_cpu]
        result = pistolero.play(self.mock_gen_player, 0)
        mock_print.assert_any_call("Sientes un dolor y calor que se extiende en tu pierna.")
        self.assertEqual(self.mock_in_player.hp, 0)
        self.assertEqual(result, 0)

    def test_Dis_Rec(self, mock_Player_class, mock_print):
        self.mock_in_player.player_choose_move.return_value = 3
        self.mock_in_cpu.cpu_choose_move.return_value = 2
        mock_Player_class.side_effect = [self.mock_in_player, self.mock_in_cpu]
        result = pistolero.play(self.mock_gen_player, 0)
        mock_print.assert_any_call("Agarras a tu enemigo tratando de recargar y das en el blanco.")
        self.assertEqual(self.mock_in_cpu.hp, 0)
        self.assertEqual(result, 1)

    def test_Cub_loss(self, mock_Player_class, mock_print):
        self.mock_in_player.player_choose_move.side_effect = [1, 1, 1, 2]
        self.mock_in_cpu.cpu_choose_move.side_effect = [1, 2, 3, 3]
        mock_Player_class.side_effect = [self.mock_in_player, self.mock_in_cpu]
        test_calls = [call("Se miran fijamente ambos protegiendose"),
                      call("Te apresuras a cubrirte pero tu enemigo aprovecha esta oportunidad para recargar."),
                      call("Excelentes reflejos! Logras evitar que esa bala diera en el blanco"),
                      call("Sientes un dolor y calor que se extiende en tu pierna.")]
        result = pistolero.play(self.mock_gen_player, 0)
        mock_print.assert_has_calls(test_calls)
        self.mock_in_player.recharge.asssert_not_called()
        self.mock_in_player.shoot.asssert_not_called()
        self.mock_in_cpu.recharge.assert_called_once()
        self.mock_in_cpu.shoot.assert_called_once()
        self.assertEqual(result, 0)

    def test_Rec_loss(self, mock_Player_class, mock_print):
        self.mock_in_player.player_choose_move.return_value = 2
        self.mock_in_cpu.cpu_choose_move.side_effect = [1, 2, 3]
        mock_Player_class.side_effect = [self.mock_in_player, self.mock_in_cpu]
        test_calls = [call("En cuanto tocas tu pistola, tu rival se cubre. Tranquilamente recargas."),
                      call("Logras cargar tu arma y notas que tu rival hizo lo mismo."),
                      call("Sientes un dolor y calor que se extiende en tu pierna.")]
        result = pistolero.play(self.mock_gen_player, 0)
        mock_print.assert_has_calls(test_calls)
        self.assertEqual(self.mock_in_player.recharge.call_count, 2)
        self.mock_in_player.shoot.asssert_not_called()
        self.mock_in_cpu.recharge.assert_called_once()
        self.mock_in_cpu.shoot.asssert_not_called()
        self.assertEqual(result, 0)

    def test_Dis_win(self, mock_Player_class, mock_print):
        self.mock_in_player.player_choose_move.return_value = 3
        self.mock_in_cpu.cpu_choose_move.side_effect = [1, 3, 2, 1]
        mock_Player_class.side_effect = [self.mock_in_player, self.mock_in_cpu]
        test_calls = [
            call("Justo antes de jalar el gatillo ves como tu enemigo alcanza a cubrirse, una bala desperdiciada"),
            call("Ambos disparan a la vez y las balas chocan entre si."),
            call("Agarras a tu enemigo tratando de recargar y das en el blanco.")]
        result = pistolero.play(self.mock_gen_player, 0)
        mock_print.assert_has_calls(test_calls)
        self.assertEqual(self.mock_in_player.player_choose_move.call_count, 3)
        self.mock_in_player.recharge.asssert_not_called()
        self.assertEqual(self.mock_in_player.shoot.call_count, 2)
        self.mock_in_cpu.recharge.asssert_not_called()
        self.mock_in_cpu.shoot.assert_called_once()
        self.assertEqual(result, 1)
        

if __name__ == '__main__':
    unittest.main()
