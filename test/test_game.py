import sys
import unittest
from unittest.mock import patch
from io import StringIO
from notecircle import NoteCircle

class TestNoteCircleLogic(unittest.TestCase):
  def setUp(self):
    self.game = NoteCircle()

  @patch('sys.stdout', new_callable=StringIO)
  def assert_output(self, expected_output, mock_stdout):
    game = NoteCircle()
    game.play_game()
    self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

  @patch('builtins.input', side_effect=['quit'])
  def test_quit_game(self, mock_input):
    with patch('random.choice', side_effect=['D', 'Eb']):
      expected_output = "Thanks for playing! Goodbye."
      self.assertRaises(SystemExit)
      sys.stdout.flush()

  def test_get_random_notes(self):
    note1, note2 = self.game.get_random_notes()
    self.assertIsInstance(note1, str)
    self.assertIsInstance(note2, str)

  def test_resolve_enharmonic_returns_one_of_the_possible_notes(self):
    note = self.game.resolve_enharmonic(['A#', 'Bb'])
    self.assertIn(note, ['A#', 'Bb'])

  def test_calculate_semitones_returns_the_correct_number(self):
    note1 = 'C'
    note2 = 'E'
    expected_semitones = 4
    actual_semitones = self.game.calculate_semitones(note1, note2)
    self.assertEqual(expected_semitones, actual_semitones)

  def test_find_note_index_returns_the_correct_index(self):
    note = 'C'
    expected_index = 3
    actual_index = self.game.find_note_index(note)
    self.assertEqual(expected_index, actual_index)

  def test_find_note_index_raises_value_error_if_note_is_not_in_the_list(self):
    note = 'H'
    with self.assertRaises(ValueError):
      self.game.find_note_index(note)

class TestNoteCircleInput(unittest.TestCase):
  def setUp(self):
    self.game = NoteCircle()

  @patch('sys.stdout', new_callable=StringIO)
  def assert_output(self, expected_output, mock_stdout):
    game = NoteCircle()
    game.play_game()
    self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

  @patch('builtins.input', side_effect=['2', '-1', ''])
  def test_valid_and_invalid_guesses(self, mock_input):
    with patch('random.choice', side_effect=['C', 'D']):
        expected_outputs = [
            "Congratulations! Your guess is correct.",
            "Invalid input. Please enter a number, 'give up', or 'quit'.",
            "Invalid input. Please enter a number, 'give up', or 'quit'.",
        ]
        for expected, input in zip(expected_outputs, mock_input):
            self.assert_output(expected)

  def test_calculate_semitones_returns_the_correct_number_enharmonic(self):
    note1 = 'C#'
    note2 = 'Db'
    expected_semitones = 0
    actual_semitones = self.game.calculate_semitones(note1, note2)
    self.assertEqual(expected_semitones, actual_semitones)

if __name__ == '__main__':
  unittest.main()
