import random

correct = 'you guessed correctly!'
too_low = 'Too Low!!'
too_high = 'too high'

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 1000


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''

    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    times_guessed = 0

    while True:
        try:
            guess = get_guess()
            result = check_guess(guess, secret)
            times_guessed = times_guessed + 1
            print(f"{result}, times guessed: {times_guessed}")

            if result == correct:
                break
        except:
            print('An exception occured!')
            break
    
    play_again = input("Would you like to play again? (enter y for yes or n for no) ")

    while play_again.lower() not in { 'y' , 'n' }:
        play_again = input("Would you like to play again? (enter y for yes or n for no) ")

    if play_again.lower() == "y":
        main()
        
    else:
        print("Thanks for playing! Bye bye!")


if __name__ == '__main__':
    main()
