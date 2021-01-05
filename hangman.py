import random
import time

words = ['computer', 'random', 'hangman', 'programming', 'laptop', 'internet', 'artificial', 'serene']


def iswinner(l1, l2):
    if l1 == l2:
        return True
    else:
        return False


def stats(tot, tr):
    print("Remaining tries : ", tot - tr)


def main():
    print("Welcome to the Hangman Game ! We're searching a random word for you....")
    time.sleep(1)
    word = random.choice(words)
    word_list = list(word)
    blank_list = ['_' for i in range(len(word))]
    guessed_letters = []

    tries = 0
    total = 6

    while tries != total:
        stats(total, tries)
        print(' '.join(blank_list))
        if not iswinner(blank_list, word_list):
            guess = input('Please guess a letter : ').strip()
            if len(guess) != 1:
                print("Invalid input, please try again...")
                continue

            elif guess in guessed_letters:
                print("You have already guessed that letter.\n You have guessed : ", ' ,'.join(guessed_letters))
                continue
            else:
                guessed_letters.append(guess)
                if guess in word_list:
                    print("Right Guess..")
                    pos = word_list.index(guess)
                    occ = word_list.count(guess)
                    blank_list[pos] = guess
                    if occ > 1:
                        wl_copy = word_list[:]
                        n_list = wl_copy[pos + 1:]
                        c = 1
                        for letter in n_list:
                            if letter == guess:
                                blank_list[pos + c] = guess
                            c += 1
                else:
                    print("Oops,Wrong Guess..")
                    tries += 1
                    continue
            print('')
        else:
            print("Congratulations !! You won .")
            break

    if tries == total:
        print("You are out of guesses..")
        print("The right word is : ", word)

    p_again = input("Do you want to play again ? (Y/N) : ")
    if p_again.upper() == "Y":
        main()


main()
