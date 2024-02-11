import random
import hangmanArt

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    

endOfGame = False
wordList = ["ardvark", "baboon", "camel"]
chosenWord = random.choice(wordList)
wordLength = len(chosenWord)

#set lives to 6 so you can increment the hangman on mistakes
lives = 6

#for testing only
print(f"For the test the word is: {chosenWord}")

display = []
for _ in range(wordLength):
    display.append("_")

print(f"Guess a word that matches this: \n", (display))

while not endOfGame: 
    guess = input("\n Guess a letter: ").lower()

    for position in range(wordLength):
        letter = chosenWord[position]
        # print(f"Position: {position}\n Letter: {letter}\n Guess: {(guess)}")
        if letter == guess:
            display[position] = letter
    if guess not in chosenWord:
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You lose.")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        endOfGame = True
        print("You win!")
        
    print(stages[lives])
