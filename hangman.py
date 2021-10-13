import random

play = True


def keep_playing(message):
    print(message)
    playing = input("\nKeep playing? (Y/N): ")
    global play
    if playing.lower().startswith('y'):
        play = True
    elif playing.lower().startswith('n'):
        play = False


while play:

    words_list = [
        'piano',
        'table',
        'television',
        'computer',
        'glasses'
    ]

    good_list = [
        'excellent',
        'great',
        'nice',
        'nice one',
        'good',
        'awesome'
    ]

    bad_list = [
        'oops',
        'oopsie',
        'bummer',
        'that\'s a shame',
        'sorry',
        'i\'m sorry'
    ]

    word = random.choice(words_list)

    tries = 5

    print(f'\nWord: {word}')

    print(len(word) * '_ ')

    correct_guesses = []
    wrong_guesses = []

    while tries > 0:
        if not correct_guesses and tries == 5:
            guess = input("\nEnter a letter or enter 'hint' to get a hint: ")
            if guess == 'hint':
                print(f"\nHere's a hint...")
                guess = random.choice(list(word))
        else:
            guess = input("\nEnter a letter: ")

        if guess.isalpha():
            if guess in correct_guesses:
                print(f"\nAlready guessed\n{tries} tries left\n")
            elif guess == 'hint':
                print(f"\nSorry, can only use 'hint' on first turn\n{tries} tries left\n")
            elif guess in wrong_guesses:
                print(f"\nAlready tried, not in word\n{tries} tries left\n")
            elif guess not in word:
                bad = random.choice(bad_list).capitalize()
                wrong_guesses.append(guess)
                tries -= 1
                print(f"\n{bad}, {guess.upper()} is not in the word\n{tries} tries left\n")
                if tries == 0:
                    keep_playing("You've lost")
                    play = False
                    break
            else:
                good = random.choice(good_list).capitalize()
                print(f"\n{good}, {guess.upper()} is in the word\n{tries} tries left\n")
                correct_guesses.append(guess)
        else:
            print(f"\nSorry, {guess} is not a valid guess\n{tries} tries left\n")

        print_word = ""

        # print the word with guesses
        for x in word:
            if x in correct_guesses:
                print_word += x + " "
            else:
                print_word += "_ "
        print(print_word)

        won = True
        for letter in word:
            if letter not in correct_guesses:
                won = False
                break

        if won:
            keep_playing("You've won!")
            break
