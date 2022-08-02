import wordle

NUMBER_OF_GAMES = 10
NUMBER_OF_ROUNDS = 6

wins = 0

for game in range(NUMBER_OF_GAMES):
    wordlelist = wordle.WordList(wordle.FILENAME_ALL, wordle.FILENAME_POSSIBLE)
    wordlist = wordlelist.return_word_list()
    correct = wordlelist.return_random_word()

    guess = wordlist[0]
    for round in range(NUMBER_OF_ROUNDS):
        guess_wordle = wordle.Guess(guess, correct)


        result = guess_wordle.give_result()
        wordlelist.update_wordlist(result, guess)
        wordlist = wordlelist.return_word_list()
        guess = wordlist[0]

        if guess_wordle.guessed:
            wins+=1
            break

    print(f'Game number {game + 1} passed')

print(f"Number of wins: {wins}")
print(f"Win ratio: {wins/NUMBER_OF_GAMES}")