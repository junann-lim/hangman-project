from replit import clear
import random
import hangman_art
import hangman_words

print(hangman_art.logo)

from hangman_words import word_list
chosen_word = random.choice(word_list)

#print(f"The chosen word is {chosen_word}.")

display = []
num_letters = len(chosen_word)
for _ in range(num_letters):
  display += "_"

lives = 6

end_of_game = False 

while not end_of_game: 
  guess = input("Guess a letter: ").lower()

  clear()
  
  if guess in display:
    print(f"You've already guessed {guess}.")

  for position in range(num_letters):
    letter = chosen_word[position]
    if letter == guess: 
      display[position] = letter

  if guess not in chosen_word:
    print(f"You've guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  print(f"{' '.join(display)}")
  
  if "_" not in display:
    end_of_game = True 
    print("You win.")

  print(hangman_art.stages[lives])
