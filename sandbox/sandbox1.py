# Python 3.11.2 Official Documentation
# https://docs.python.org/3/index.html
# > Sample codes grow in complexity: https://wiki.python.org/moin/SimplePrograms

# Learning from the Professionals
# ==============================================================================
# control+click the name of the module to open it and see how the developers
# of the Python wrote them
# import math
# import string
# import sys
import glob


# Print content of the files in a given directory
# from: https://wiki.python.org/moin/SimplePrograms
# ==============================================================================
def print_files_content(dirPath: str, fileExtension: str) -> None:
    python_files = glob.glob(dirPath + '*.' + fileExtension)
    for file_name in sorted(python_files):
        print ('    ------' + file_name)

        with open(file_name) as f:
            for line in f:
                print ('    ' + line.rstrip())

        print()

# if __name__ == '__main__':
#     import glob  # glob supports Unix style pathname extensions
#     print_files_content('.\\..\\strings\\', 'py')


# Working with time
# from: https://wiki.python.org/moin/SimplePrograms
# ==============================================================================

def print_local_time() -> None:
    from time import localtime

    time_now = localtime()
    print(time_now)
    hour = time_now.tm_hour
    print(hour)

# if __name__ == '__main__':
#     print_local_time()


# Using Doctest-based testing
# from: https://wiki.python.org/moin/SimplePrograms
# ==============================================================================
def median(pool) -> None:
    '''Statistical median to demonstrate doctest.
    >>> median([2, 9, 9, 7, 9, 2, 4, 5, 8])
    6 # change to 7 to pass the test
    '''
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    else:
        return (copy[int(size/2 - 1)] + copy[int(size/2)]) / 2

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()


# Guess the number game
# from: https://wiki.python.org/moin/SimplePrograms
# ==============================================================================
def number_guessing_game(name: str) -> None:
    import random
    guesses_made = 0


    number = random.randint(1, 20)
    print ('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

    while guesses_made < 6:

        guess = int(input('Take a guess: '))

        guesses_made += 1

        if guess < number:
            print ('Your guess is too low.')

        if guess > number:
            print ('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
    else:
        print ('Nope. The number I was thinking of was {0}'.format(number))

# if __name__ == '__main__':
#     name = input('Hello! What is your name?')
#
#     cont = 'y'
#     while(cont.lower() != 'n'):
#         number_guessing_game(name)
#         cont = input("Plan again (Y/N)? ")

