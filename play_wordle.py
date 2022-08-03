import wordle

NUMBER_OF_GAMES = 1000
NUMBER_OF_ROUNDS = 6

wins = 0

for game in range(NUMBER_OF_GAMES):
    wordlelist = wordle.WordList(wordle.FILENAME_ALL, wordle.FILENAME_POSSIBLE)
    wordlist = wordlelist.return_word_list()
    correct = wordlelist.return_correct()


    guess = wordlelist.best_positional_word()
    for round in range(NUMBER_OF_ROUNDS):
        guess_wordle = wordle.Guess(guess, correct)

        # print(wordlist)
        # print(guess)

        result = guess_wordle.give_result()
        wordlelist.update_wordlist(result, guess)
        wordlist = wordlelist.return_word_list()
        guess = wordlelist.best_positional_word()

        if guess_wordle.guessed:
            wins += 1
            break

    print(f"Game: {game + 1}")

print(wins)

# def simulation(number_of_games, simulation_type = "default"):
#     pass
#
# def main():
#     """ Run the whole game """
#     simulation(10, simulation_type="words score")
#
# main()