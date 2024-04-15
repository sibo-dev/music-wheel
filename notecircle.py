import random
import sys

class NoteCircle:
  def __init__(self):
    self.notes = ['A', ['A#', 'Bb'], 'B', 'C', ['C#', 'Db'], 'D', ['D#', 'Eb'], 'E', 'F', ['F#', 'Gb'], 'G', ['G#', 'Ab']]
    self.current_notes = None

  def get_random_notes(self):
    note1 = random.choice(self.notes)
    note2 = random.choice(self.notes)
    return self.resolve_enharmonic(note1), self.resolve_enharmonic(note2)

  def resolve_enharmonic(self, note):
    if isinstance(note, list):
      return random.choice(note)
    else:
      return note

  def calculate_semitones(self, note1, note2):
    index1 = self.find_note_index(note1)
    index2 = self.find_note_index(note2)
    semitones = abs(index2 - index1)
    return semitones

  def find_note_index(self, note):
    for i, n in enumerate(self.notes):
      if isinstance(n, list) and note in n:
        return i
      elif n == note:
        return i
    raise ValueError(f"{note} is not in the list of notes.")
  
  def get_user_input(self, note1, note2):
    return input(f"How many semitones between {note1} and {note2}? (Type 'give up' to reveal the answer or 'quit' to exit): ")
  
  def process_user_input(self, user_input, correct_answer):
    if user_input.lower() == 'give up':
      print(f"The correct answer is {correct_answer} semitones.")
      self.current_notes = None
    elif user_input.lower() == 'quit':
      print("Thanks for playing! Goodbye.")
      sys.exit(0)
    else:
      try:
        user_guess = int(user_input)
        if user_guess == correct_answer:
          print("Congratulations! Your guess is correct.")
          self.current_notes = None
        else:
          print("Incorrect guess. Try again.")
      except ValueError:
        print("Invalid input. Please enter a number, 'give up', or 'quit'.")

  def play_game(self):
    while True:
      note1, note2 = self.get_random_notes()
      user_input = self.get_user_input(note1, note2)
      correct_answer = self.calculate_semitones(note1, note2)
      self.process_user_input(user_input, correct_answer)

if __name__ == "__main__":
  game = NoteCircle()
  game.play_game()
