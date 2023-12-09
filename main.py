import random
from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear

def choose_word(word_list):
  """Randomly selects a word from the word list."""
  return random.choice(word_list)

def initialize_display(word_length):
  """Creates the initial display with blanks for the chosen word."""
  return ["_" for _ in range(word_length)]

def update_display(chosen_word, display, guess):
  """Updates the display with the guessed letter if it is in the chosen word."""
  for position, letter in enumerate(chosen_word):
      if letter == guess:
          display[position] = letter
  return display

def get_user_guess():
  """Prompts the user to guess a letter and returns it."""
  return input("Guess a letter: ").lower()

def display_status(display):
  """Displays the current status of the word to the player."""
  print(f"{' '.join(display)}")

def hangman_game():
  """Main function to run the Hangman game."""
  print(logo)
  chosen_word = choose_word(word_list)
  word_length = len(chosen_word)
  display = initialize_display(word_length)
  lives = 6
  end_of_game = False

  print(f'Pssst, the solution is {chosen_word}.')

  while not end_of_game:
      guess = get_user_guess()

      if guess in display:
          print(f"You've already guessed {guess}.")
          continue

      display = update_display(chosen_word, display, guess)

      if guess not in chosen_word:
          print(f"You guessed {guess}, that's not in the word. You lose a life.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")
              break

      display_status(display)

      if "_" not in display:
          end_of_game = True
          print("You win.")

      print(stages[lives])

if __name__ == "__main__":
  hangman_game()
