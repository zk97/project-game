import unittest
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


if __name__ == '__main__':
    unittest.main()
