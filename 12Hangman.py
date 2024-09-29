import random

def get_word():
    words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'orange', 'papaya', 
             'peach', 'pineapple', 'plum', 'raspberry', 'strawberry', 'vanilla', 'watermelon']
    return random.choice(words)

def display_word(word, guessed):
    return ''.join([char if char in guessed else '_' for char in word])

def play_game():
    word = get_word()
    guessed = set()
    attempts = 10
    
    while attempts > 0:
        print(f'Attempts remaining: {attempts}')
        print(display_word(word, guessed))
        guess = input('Guess a letter: ').lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print('Invalid guess. Please guess a letter.')
            continue

        if guess in guessed:
            print('You already guessed that letter.')
            continue

        guessed.add(guess)
        
        if guess in word:
            print('Correct')
            if set(word).issubset(guessed):
                print(f'Congratulations! You guessed the word: {word}')
                break
        else:
            attempts -= 1
            print('Incorrect')
    
    if attempts == 0:
        print(f'Sorry, you ran out of attempts. The word was: {word}')

if __name__ == '__main__':
    play_game()
