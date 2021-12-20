import random

def generate_answer(level):
    answer = 0

    if level == 1:
        answer = random.randint(1, 10)
    elif level == 2:
        answer = random.randint(1, 100)
    elif level == 3:
        answer = random.randint(1, 1000)
    return answer

def validate_input(guess):
    guess = str.strip(guess)

    try:
        guess = int(guess)
    except:
        return (False, guess)
    
    return (True, guess)

def start():
    while True:
        print('Let\'s play Guess the Number.')

        level = int(input('Pick a difficulty level (1, 2, or 3): '))
        answer = generate_answer(level)

        counter = 0

        print('I have my number. What\'s your guess?', end='')

        while True:
            guess = input('')
            counter = counter + 1
            (is_valid, guess) = validate_input(guess)

            if  is_valid is False:
                continue

            if guess == answer:
                print(f'You got it in {counter} guesses.')
                break
            elif guess > answer:
                print('Too high. Guess again: ', end='')
            elif guess < answer:
                print('Too low. Guess again: ', end='')

        again = input('Play again?')

        if again == 'n':
            print('Goodbye!')
            break
    
start()