import random
import string
import os 


def load_words():
    word_list = open("words.txt", 'r').readline().split()
    return word_list

def choose_word_random(word_list):
    return random.choice(word_list)


def is_word_guessed(gameword, letters_already_guessed):
    if set(gameword) & set(letters_already_guessed) == set(gameword):
        return True
    else:
        return False

def get_guessed_word(gameword, letters_already_guessed):
    result_list = []
    for i in range(len(list(gameword))):
        if list(gameword)[i] in set(letters_already_guessed):
            result_list.append(list(gameword)[i])
        else:
            result_list.append("_ ")
    return ''.join(map(str, result_list))


def get_available_letters(letters_already_guessed):
    available_list = list(string.ascii_lowercase)
    for i in range(-len(available_list), 0):
        if available_list[i] in letters_already_guessed:
            del available_list[i]
    return ''.join(map(str, available_list))


def hints_match(word_to_match, word_from_the_list):
    word_to_match_list = list(word_to_match.replace(" ", ""))
    word_from_the_list_list = list(word_from_the_list)
    if len(word_to_match_list) != len(word_from_the_list_list):
        return False
    else:
        counter = 0
        for i in range(0, len(word_to_match_list)):
            if word_to_match_list[i] == "_":
                if word_from_the_list_list[i] not in word_to_match_list:
                    counter += 1
            elif word_to_match_list[i] == word_from_the_list_list[i]:
                counter += 1
        if counter == len(word_to_match.replace(" ", "")):
            return True
        else:
            return False


def show_possible_matches(word_to_match):
    possible_matches=[]
    for word in word_list:
        if hints_match(word_to_match, word):
            possible_matches.append(word)
    if len(possible_matches) == 0:
        return "No matches found"
    else:
        return " ".join(possible_matches)



def hangman(gameword):
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3

    print("Welcome!\n"
          "A gameword is", len(gameword), "letters long:)", "\n")
    while True:
        if not is_word_guessed(gameword, letters_guessed):
            print("You have", int(guesses_remaining), "guess(es) left and", int(warnings_remaining), "warning(s) left!")
            print("Available letters:",get_available_letters(letters_guessed))
            print("\nGame word:", get_guessed_word(gameword, letters_guessed))
            print('\n------------------------------------------------\n')

            guess = str.lower(input("Please, input a letter: "))

            if not guess.isalpha():
                if guess == "!":
                    print("Possible word matches are:",
                          show_possible_matches(get_guessed_word(gameword, letters_guessed)))
                else:
                    print("That is not a valid symbol.\n")

                    if warnings_remaining <= 0:
                        print("You have no warnings left so you lose 1 guess:_(")
                        guesses_remaining -= 1
                    else:
                      warnings_remaining -= 1
                      print("You loose 1 warning:_(")

                press = input('Press any key to continue')
                os.system('cls||clear')
            elif guess in set(letters_guessed):

                print("Oops! You`ve already guessed that letter.\n", end="")
                if warnings_remaining <= 0:
                    print("You have no warnings left so you lose 1 guess:_(")
                    guesses_remaining -= 1
                else:
                  warnings_remaining -= 1
                  print("You loose 1 warning:_(")
                press = input('Press any key to continue')
                os.system('cls||clear')
            elif guess in set(gameword):
                print("Super! Good guess!")
                letters_guessed.append(guess)
                press = input('Press any key to continue')
                os.system('cls||clear')
            else:
                letters_guessed.append(guess)
                print("Oops! That letter is not in my word.")
                print("You loose 1 guess :_(")
                guesses_remaining -= 1
                press = input('Press any key to continue')
                os.system('cls||clear')
            if guesses_remaining <= 0:
                print("Sorry, you ran out of guesses. The word was", gameword)
                break

        else:
            print("Congratulations, you won!\n")
            print("The gameword is: ", gameword)
            break



if __name__ == "__main__":

     word_list = load_words()
     gameword = choose_word_random(word_list)
     hangman(gameword)