import unittest
from unittest.mock import patch, seal, Mock
import src.minijuegos.trampas as trampas


@patch('src.minijuegos.trampas.scream', Mock())
@patch('src.minijuegos.trampas.time.sleep', Mock())
@patch('src.minijuegos.trampas.threading.Thread', Mock())
class TestTrampasClass(unittest.TestCase):
    def setUp(self):
        self.trampa = trampas.Trampas()

    def test_base_stats(self):
        expected_arrows = {"derecha": f"{('> ' * 12).ljust(38)}\n" * 10,
                           "izquierda": f"{('< ' * 12).rjust(38)}\n" * 10,
                           "abajo": ('v ' * 38 + '\n') * 5,
                           "arriba": ('^ ' * 38 + '\n') * 5,
                           "espacios": '\n' * 5}
        self.assertFalse(self.trampa.stop_threads)
        self.assertTrue(self.trampa.escape)
        self.assertEqual(self.trampa.damage, 0)
        self.assertEqual(self.trampa.move, '')
        self.assertEqual(self.trampa.arrows, expected_arrows)

    @patch('src.minijuegos.trampas.input')
    def test_count_space_stoped(self, mock_input):
        mock_input.side_effect = [' ', '  ', '', ' ', ' ', '', ' ']
        self.trampa.stop_threads = True
        self.trampa.count_space(3)
        self.assertEqual(mock_input.call_count, 1)
        self.assertTrue(self.trampa.stop_threads)

    @patch('src.minijuegos.trampas.input')
    def test_count_space_finished(self, mock_input):
        mock_input.side_effect = [' ', '  ', '', ' ', ' ', '', ' ']
        self.trampa.count_space(3)
        self.assertEqual(mock_input.call_count, 5)
        self.assertTrue(self.trampa.stop_threads)

    @patch('src.minijuegos.trampas.print')
    def test_goblins_stoped(self, mock_print):
        self.trampa.stop_threads = True
        self.trampa.goblins()
        self.assertEqual(mock_print.call_count, 1)
        self.assertTrue(self.trampa.stop_threads)
        self.assertTrue(self.trampa.escape)

    @patch('src.minijuegos.trampas.print')
    def test_goblins_finished(self, mock_print):
        self.trampa.goblins()
        self.assertIn(mock_print.call_count, range(18, 24))
        self.assertTrue(self.trampa.stop_threads)
        self.assertFalse(self.trampa.escape)

    @patch('src.minijuegos.trampas.print', Mock())
    @patch('src.minijuegos.trampas.slow_print')
    def test_run_trap_tutorial_escaped(self, mock_print):
        mock_player = Mock(health=30)
        self.trampa.run_trap(mock_player, True)
        mock_print.assert_called_with('Corriste lo suficientemente rápido.')
        mock_player.receive_damage.assert_not_called()

    @patch('src.minijuegos.trampas.print', Mock())
    @patch('src.minijuegos.trampas.slow_print')
    def test_run_trap_tutorial_failed(self, mock_print):
        mock_player = Mock(health=30)
        self.trampa.escape = False
        self.trampa.run_trap(mock_player, True)
        mock_print.assert_called_with('Necesitas ser más veloz, no llegaste a tiempo.')
        mock_player.receive_damage.assert_not_called()

    @patch('src.minijuegos.trampas.print', Mock())
    @patch('src.minijuegos.trampas.slow_print')
    def test_run_trap_real_scaped(self, mock_print):
        mock_player = Mock(health=30)
        self.trampa.run_trap(mock_player, False)
        mock_print.assert_called_with('Lograste escapar de esta, que pesados son los duendes.')
        mock_player.receive_damage.assert_not_called()

    @patch('src.minijuegos.trampas.print', Mock())
    @patch('src.minijuegos.trampas.slow_print')
    def test_run_trap_real_failed(self, mock_print):
        mock_player = Mock(health=30)
        self.trampa.escape = False
        self.trampa.run_trap(mock_player, False)
        mock_print.assert_called_with('Perdiste 0 de vida')
        mock_player.receive_damage.assert_called_once()

    @patch('src.minijuegos.trampas.input')
    def test_player_moves_stoped(self, mock_input):
        mock_input.side_effect = ['A', 'S']
        self.trampa.stop_threads = True
        self.trampa.player_moves()
        mock_input.assert_called_once()
        self.assertEqual(self.trampa.move, 'a')
        self.assertTrue(self.trampa.stop_threads)

if __name__ == '__main__':
    unittest.main()
