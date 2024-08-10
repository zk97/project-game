import unittest
from unittest.mock import patch, Mock
import src.minijuegos.examen as examen


class TestLoadExamen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ans_example = {"respuesta1": True, "respuesta2": False, "respuesta3": False, "respuesta4": False}
        cls.sample_questions = {"g1": {"pregunta1": ans_example},
                                "g2": {"pregunta2": ans_example},
                                "g3": {"pregunta3": ans_example},
                                "g4": {"pregunta4": ans_example},
                                "g5": {"pregunta5": ans_example}}

    def test_load_file(self):
        self.assertEqual(examen.load_questions('tests/unit/minijuegos/test_preguntas.json'), self.sample_questions)


class TestGetQuestionsExamen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ans_example = {"respuesta1": True, "respuesta2": False, "respuesta3": False, "respuesta4": False}
        cls.sample_questions = {"g1": {"pregunta1": cls.ans_example},
                                "g2": {"pregunta2": cls.ans_example},
                                "g3": {"pregunta3": cls.ans_example},
                                "g4": {"pregunta4": cls.ans_example},
                                "g5": {"pregunta5": cls.ans_example}}

    def test_get_questions(self):
        expected_question = "pregunta1"
        result_question, result_answers = examen.get_question(self.sample_questions, 'g1')
        self.assertEqual(result_question, expected_question)
        self.assertEqual(result_answers, self.ans_example)


class TestMixExamen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ans_example = {"respuesta1": True, "respuesta2": False, "respuesta3": False, "respuesta4": False}
        cls.sample_questions = {"g1": {"pregunta1": ans_example},
                                "g2": {"pregunta2": ans_example},
                                "g3": {"pregunta3": ans_example},
                                "g4": {"pregunta4": ans_example},
                                "g5": {"pregunta5": ans_example}}

    def test_mix_choice(self):
        expected = {'respuesta1', 'respuesta2', 'respuesta3', 'respuesta4'}
        result = examen.mix_choice(self.sample_questions["g1"]["pregunta1"].keys())
        self.assertEqual(set(result), expected)
        self.assertEqual(len(result), 4)


@patch('src.minijuegos.examen.print', Mock())
@patch('src.minijuegos.examen.slow_talk')
class TestModifyExamen(unittest.TestCase):

    def setUp(self):
        self.player = Mock()
        self.player.health = 20
        self.player.magic = 28
        self.player.sword_lvl = 2
        self.player.gun_lvl = 2
        self.player.shield_lvl = 2

    def test_modify_group1(self, mock_talk):
        result = examen.modify_objects(self.player, 1)
        mock_talk.assert_called_once_with('-Eres tan inculto que pierdes todos tus objetos.')
        self.assertEqual(self.player.shield_down.call_count, 3)
        self.assertEqual(self.player.sword_down.call_count, 3)
        self.assertEqual(self.player.gun_down.call_count, 3)
        self.assertEqual(result, 0)

    @patch('src.minijuegos.examen.slow_print')
    def test_modify_group2(self, mock_print, mock_talk):
        result = examen.modify_objects(self.player, 2)
        mock_talk.assert_called_once_with('-Me haces enfurecer con tu poco conocimiento.')
        mock_print.assert_called_once_with('Te dispara una flecha al estomago.\nPierdes 0 de vida.')
        self.player.receive_damage.called_once_with(20, 0)
        self.assertEqual(self.player.magic, 0)
        self.assertEqual(result, 0)

    @patch('src.minijuegos.examen.slow_print')
    def test_modify_group3(self, mock_print, mock_talk):
        result = examen.modify_objects(self.player, 3)
        mock_talk.assert_called_once_with('-Me haces enfurecer con tu poco conocimiento.')
        mock_print.assert_called_once_with('Te dispara una flecha al estomago.\nPierdes 0 de vida.')
        self.player.receive_damage.called_once_with(15, 0)
        self.assertEqual(self.player.magic, 3)
        self.assertEqual(result, 0)

    @patch('src.minijuegos.examen.slow_print')
    def test_modify_group4(self, mock_print, mock_talk):
        result = examen.modify_objects(self.player, 4)
        mock_talk.assert_called_once_with('-Me haces enfurecer con tu poco conocimiento.')
        mock_print.assert_called_once_with('Te dispara una flecha al estomago.\nPierdes 0 de vida.')
        self.player.receive_damage.called_once_with(10, 0)
        self.assertEqual(self.player.magic, 8)
        self.assertEqual(result, 0)

    def test_modify_group5_all_max(self, mock_talk):
        self.player.sword_lvl = 3
        self.player.gun_lvl = 3
        self.player.shield_lvl = 3
        result = examen.modify_objects(self.player, 5)
        mock_talk.assert_any_call('Casi logras tener 5 respuestas correctas. ¿Qué objeto quieres que mejore '
                                  'para ti?')
        mock_talk.assert_called_with('-Veo que ya tienes todo mejorado al máximo, tal vez para la otra.')
        self.player.sword_up.assert_not_called()
        self.player.gun_up.assert_not_called()
        self.player.shield_up.assert_not_called()
        self.assertEqual(result, 1)

    @patch('src.minijuegos.examen.input')
    def test_modify_group5_sword_max_revolver(self, mock_input, mock_talk):
        self.player.sword_lvl = 3
        mock_input.side_effect = ['espada', 'revolver', 'escudo']
        result = examen.modify_objects(self.player, 5)
        mock_talk.assert_called_once_with('Casi logras tener 5 respuestas correctas. ¿Qué objeto quieres que mejore '
                                          'para ti?')
        self.player.sword_up.assert_not_called()
        self.player.gun_up.assert_called_once()
        self.player.shield_up.assert_not_called()
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(result, 1)

    @patch('src.minijuegos.examen.input')
    def test_modify_group5_sowrd(self, mock_input, mock_talk):
        mock_input.side_effect = ['espada', 'revolver', 'escudo']
        result = examen.modify_objects(self.player, 5)
        mock_talk.assert_called_once_with('Casi logras tener 5 respuestas correctas. ¿Qué objeto quieres que mejore '
                                          'para ti?')
        self.player.sword_up.assert_called_once()
        self.player.gun_up.assert_not_called()
        self.player.shield_up.assert_not_called()
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(result, 1)

    @patch('src.minijuegos.examen.input')
    def test_modify_group5_gun(self, mock_input, mock_talk):
        mock_input.side_effect = ['relvober', 'revolver']
        result = examen.modify_objects(self.player, 5)
        mock_talk.assert_called_once_with('Casi logras tener 5 respuestas correctas. ¿Qué objeto quieres que mejore '
                                          'para ti?')
        self.player.sword_up.assert_not_called()
        self.player.gun_up.assert_called_once()
        self.player.shield_up.assert_not_called()
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(result, 1)

    @patch('src.minijuegos.examen.input')
    def test_modify_group5_shield(self, mock_input, mock_talk):
        mock_input.side_effect = ['escudo']
        result = examen.modify_objects(self.player, 5)
        mock_talk.assert_called_once_with('Casi logras tener 5 respuestas correctas. ¿Qué objeto quieres que mejore '
                                          'para ti?')
        self.player.sword_up.assert_not_called()
        self.player.gun_up.assert_not_called()
        self.player.shield_up.assert_called_once()
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(result, 1)

    def test_modify_group6(self, mock_talk):
        result = examen.modify_objects(self.player, 6)
        mock_talk.assert_called_once_with('-Me pusiste de buen humor, mejoraré todos tus objetos')
        self.player.sword_up.assert_called_once()
        self.player.gun_up.assert_called_once()
        self.player.shield_up.assert_called_once()
        self.assertEqual(result, 1)


@patch('src.minijuegos.examen.mix_choice',
       Mock(return_value=["respuesta1", "respuesta2", "respuesta3", "respuesta4"]))
@patch('src.minijuegos.examen.load_questions', Mock())
@patch('src.minijuegos.examen.time.sleep', Mock())
@patch('src.minijuegos.examen.print', Mock())
@patch('src.minijuegos.examen.modify_objects')
@patch('src.minijuegos.examen.slow_print')
@patch('src.minijuegos.examen.scream')
@patch('src.minijuegos.examen.input')
class TestPlayExamen(unittest.TestCase):

    def setUp(self, ):
        ans_example = {"respuesta1": True, "respuesta2": False, "respuesta3": False, "respuesta4": False}
        patcher = patch('src.minijuegos.examen.get_question', return_value=('pregunta1', ans_example))
        self.mock_get = patcher.start()
        self.addCleanup(patcher.stop)
        self.mock_player = Mock()

    def test_tutorial_success_two_fail_three(self, mock_input, mock_scream, mock_print, mock_modify):
        mock_input.side_effect = ['j', 'a', 'A', 'd', 'c', 'b', 'k']
        result = examen.play(self.mock_player, True)
        self.assertEqual(mock_input.call_count, 6)
        self.assertEqual(mock_scream.call_count, 3)
        mock_print.assert_called_with('Tuviste 2 respuestas correctas')
        mock_modify.assert_not_called()
        self.assertIsNone(result)

    def test_real_success_two_fail_three(self, mock_input, mock_scream, mock_print, mock_modify):
        mock_input.side_effect = ['a', 'd', 'c', 'b', 'a', 'b' 'k']
        result = examen.play(self.mock_player, False)
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_scream.call_count, 3)
        mock_print.assert_called_with('Tuviste 2 respuestas correctas')
        mock_modify.assert_called_once_with(self.mock_player, 3)
        self.assertIsInstance(result, Mock)

    def test_real_success_four_fail_one(self, mock_input, mock_scream, mock_print, mock_modify):
        mock_input.side_effect = ['a', 'a', 'd', 'a', 'A', 'a', 'b' 'a']
        result = examen.play(self.mock_player, False)
        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_scream.call_count, 1)
        mock_print.assert_called_with('Tuviste 4 respuestas correctas')
        mock_modify.assert_called_once_with(self.mock_player, 5)
        self.assertIsInstance(result, Mock)


if __name__ == '__main__':
    unittest.main()
