import io
from unittest.mock import patch
import unittest
from szybkolicze.dodawanie import dodawanie


class DodawanieTestCase(unittest.TestCase):

    def test_nie_rozumie(self):
        user_input = ['2,3']
        expected_output = 'Ile to będzie 84 + 7 = ?\n' \
                          '    Nie rozumię. Podaj dwie cyfry połączone +, np.: 3+4\n' \
                          '    Nie rozumię. Podaj dwie cyfry połączone +, np.: 3+4\n' \
                          '    Nie rozumię. Podaj dwie cyfry połączone +, np.: 3+4\n'

        with patch('builtins.input', side_efect=user_input):
            with patch('sys.stdout', new=io.StringIO()) as output:
                dodawanie(84, 7)
                self.assertEqual(expected_output, output.getvalue())

    def test_dobrze(self):
        user_input = ['6+1']
        expected_output = 'Ile to będzie 84 + 7 = ?\n' \
                          '    Dobrze!\n'

        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=io.StringIO()) as output:
                dodawanie(84, 7)
                self.assertEqual(expected_output, output.getvalue())

    def test_1_dobrze(self):
        user_input = ['1+1', '6+1']
        expected_output = 'Ile to będzie 84 + 7 = ?\n' \
                          '    Niestety nie. Spróbuj jeszcze raz!\n'\
                          '    Dobrze!\n'

        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=io.StringIO()) as output:
                dodawanie(84, 7)
                self.assertEqual(expected_output, output.getvalue())

    def test_2_dobrze(self):
        user_input = ['1+1', '1+1', '6+1']
        expected_output = 'Ile to będzie 84 + 7 = ?\n' \
                          '    Niestety nie. Spróbuj jeszcze raz!\n'\
                          '    Niestety nie. Podpowiedź: Ile 4 brakuje do pełnej 10?\n'\
                          '    Dobrze!\n'

        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=io.StringIO()) as output:
                dodawanie(84, 7)
                self.assertEqual(expected_output, output.getvalue())

    def test_bezdop_dobrze(self):
        expected_output = '    Dobrze!\n'
        user_input = ['90']
        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=io.StringIO()) as output:
                dodawanie(84, 6)
                self.assertEqual(expected_output, output.getvalue())

    def test_bezdop_1_zle(self):
        expected_output = '    Niestety nie. Spróbuj jeszcze raz!\n'\
                          '    Dobrze!\n'

        user_input = ['0', '90']
        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=io.StringIO()) as output:
                dodawanie(84, 6)
                self.assertEqual(expected_output, output.getvalue())

    def test_bezdop_nie_udalo_sie(self):
        expected_output = '    Niestety nie. Spróbuj jeszcze raz!\n' \
                          '    Niestety nie. Spróbuj jeszcze raz!\n' \
                          '    Niestety nie. Spróbuj jeszcze raz!\n' \
                          "    Niestety nie udało się :(. 84 + 6 = 90\n"

        user_input = ['0', '0', '0', '0']
        with patch('builtins.input', side_effect=user_input):
            with patch('sys.stdout', new=io.StringIO()) as output:
                dodawanie(84, 6)
                self.assertEqual(expected_output, output.getvalue())
