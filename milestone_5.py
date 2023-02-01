import random
class Hangman:
   def __init__(self,word_list,num_lives = 5):
      self.word_list = word_list
      self.num_lives = num_lives
      self.word = random.choice(self.word_list)   
      self.word_guessed = ["_"]*len(self.word)
      self.num_letters = len(self.word)
      self.list_of_guesses = [ ]
   
   def check_guess(self,guess):
      self.guess = guess.lower()
      self.list_of_guesses.append(guess)
      if guess in self.word:
         print(f"Good guess! {guess} is in the word.")

         for letter in range(len(self.word)):     
               if self.word[letter] == guess:
                  self.word_guessed[letter]=guess
                  self.num_letters-=1  
                  print(self.num_letters)
         print (f"The word list is {self.word_guessed}")
      else:
         self.num_lives-=1
         print(f"Sorry, {guess} is not in the word.")
         print(f"You have {self.num_lives} lives left.")
               
   def ask_for_input(self):
      while True:
         guess = input("enter a letter")
         if len(guess)!= 1 and not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
         elif guess in self.list_of_guesses:
            print("You already tried that letter!")
         else:
          self.check_guess(guess)
          break

def play_game(word_list):
      num_lives = 5
      game = Hangman(word_list, num_lives)
      print(game.word_guessed)
      print(game.word_list)
      print(game.word)
      print(game.list_of_guesses)
      #game.ask_for_input()
      while True:
         if game.num_lives == 0:
            print('You lost!')
            break
         elif game.num_letters >0:
            game.ask_for_input()
         else:
            print('Congratulations. You won the game!')
            break

word_list = ['banana','mango','apple','orange'] 
play_game(word_list)
