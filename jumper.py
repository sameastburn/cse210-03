import random

class Jumper:
  _playing = True

  def start(self):
    word = Word()
    word.print_current_guess()
    word.set_random_word()

    man = ParachuteMan()

    gameover = GameOver()

    while self._playing:
      man.draw_parachute_man()
      
      if man.get_lives() == 0:
        self._playing = False
      else:
        check = word.check_input()

        if (not check):
          man.set_lives(man.get_lives() - 1)

      if (gameover.check_game_over(word.get_current_guess())):
        self._playing = False

class Word:
  current_guess = '_____'
  random_word = ''

  def get_input(self):
    user_input = input('Guess a letter [a-z]: ')

    return user_input
  
  def set_random_word(self):
    self.random_word = random.choice(['light', 'might', 'white', 'flake', 'poise'])
  
  def check_input(self):
    print('')
    letter_guess = self.get_input()

    ret = True

    if (letter_guess != '' and letter_guess in self.random_word):
      pos = self.random_word.find(letter_guess)
      self.current_guess = self.current_guess[:pos] + letter_guess + self.current_guess[pos + 1:]
    else:
      ret = False

    self.print_current_guess()

    return ret

  def print_current_guess(self):
    print('')
    
    new_string = ''
    for letter in self.current_guess:
      new_string = new_string + letter + ' '

    print(new_string)

    print('')

  def get_current_guess(self):
    return self.current_guess

class ParachuteMan:
  _lives = 4

  def draw_parachute_man(self):
    if (self._lives == 4):
      print("  ---")
      print(" /---\\")
      print(" \   /")
      print("  \ /")
      print("   0")
    elif (self._lives == 3):
      print(" /---\\")
      print(" \   /")
      print("  \ /")
      print("   0")
    elif (self._lives == 2):
      print(" \   /")
      print("  \ /")
      print("   0")
    elif (self._lives == 1):
      print("  \ /")
      print("   0")
    elif (self._lives == 0):
      print("   x")

    print("  /|\\")
    print("  / \\")
    print("\n^^^^^^^")
  
  def get_lives(self):
    return self._lives

  def set_lives(self, lives):
    self._lives = lives

class GameOver:
  def check_game_over(self, end_string):
    if ('_' in end_string):
      return False
    else:
      return True

def main():
  jumper = Jumper()
  jumper.start()

main()
