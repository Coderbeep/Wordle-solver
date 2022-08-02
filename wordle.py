import random

FILENAME_ALL = "all_words.txt"
FILENAME_POSSIBLE = "words.txt"

class Guess:
    def __init__(self, guess_word, correct_word):
        self.guess_word = guess_word
        self.correct_word = correct_word

        self.guessed = False
        self.result = self.give_result()

    def __str__(self):
        """ String representation of the guess
        G, Y, _ mean right spot, misplaced, no"""
        representation = ""
        for letter in self.result:
            if(letter == 2):
                representation +="G"
            elif(letter == 1):
                representation += "Y"
            else:
                representation += "_"

        return representation

    def give_result(self):
        """ Gives 0/1/2 representation of the guess
        according to the correct word
        0 - no / 1 - misplaced / 2 - right """
        result = [0,0,0,0,0]
        for i, letter in enumerate(self.guess_word):
            if(letter in self.correct_word): result[i]=1

        for i, letter in enumerate(self.guess_word):
            if(letter == self.correct_word[i]): result[i]=2

        if(result == [2,2,2,2,2]):
            self.guessed = True
        return result


class WordList():
    def __init__(self, filename_all, filename_possible):
        self.filename_all = filename_all
        self.filename_possible = filename_possible

        with open(filename_all) as file:
            self.word_list = [x.strip() for x in file]

        with open(filename_possible) as file:
            self.possible_word_list = [x.strip() for x in file]

        self.possitional_letter_count = {}
        self.letters_count = {}
        self.words_score = {}

    def return_word_list(self):
        'Return the list of words which are still available'
        return self.word_list

    def return_random(self):
        return random.choice(self.word_list)

    def return_correct(self):
        'Returns a random word from the list; used only to determine the correct word at the beginning'
        return random.choice(self.possible_word_list)

    def update_wordlist(self, guess_numbers, guess):
        'Update the available words list according to guesses'
        temp_wordlist = self.word_list.copy()

        'Seek for letters that are misplaced in that guess'
        misplaced_letters = []
        misplaced_letters_index = []
        for index, letter in enumerate(guess):
            if(guess_numbers[index] == 1):
                misplaced_letters.append(letter)
                misplaced_letters_index.append(index)

        'Seek for letter that are wrong'
        wrong_letters = []
        for index, letter, in enumerate(guess):
            if(guess_numbers[index]==0):
                wrong_letters.append(letter)

        'Remove words that do not match with G places'
        for i, number in enumerate(guess_numbers):
            if(number == 2):
                for word in self.word_list:
                    if(guess[i]!=word[i]):
                        if word in temp_wordlist:
                            temp_wordlist.remove(word)
        self.word_list = temp_wordlist

        'Remove words that do not match with Y spots'
        if len(misplaced_letters)!=0:
            words = []
            for word in self.word_list:
                proper = True
                for letter, index in zip(misplaced_letters, misplaced_letters_index):
                    if letter not in word or letter == word[index]: proper = False
                if proper:
                    words.append(word)
            self.word_list = words

        'Remove words that contain letter that are wrong'
        if len(wrong_letters)!=0:
            words = []
            for word in self.word_list:
                proper = True
                for letter in wrong_letters:
                    if letter in word: proper = False
                if proper:
                    words.append(word)
            self.word_list = words

############################################################################################
    "Instead of choosing the first word from the list of possible ones, I will use different approach"
    "I will create a method that counts every occurrance of letter in the list, and generate score"
    "for every word, basing on those counts."
    def generate_letter_count(self):
        self.letters_count = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
        for word in self.word_list:
            for letter in set(word):
                self.letters_count[letter] += 1

    def generate_word_scores(self):
        self.generate_letter_count()
        self.words_score = {}
        for word in self.word_list:
            word_score = 0
            letters_set = set(word)
            for letter in letters_set:
                word_score += self.letters_count[letter]
            self.words_score[word] = word_score

    def best_word(self):
        self.generate_word_scores()
        best_words = []
        maximum = max(self.words_score.values())
        for word, score in self.words_score.items():
            if score == maximum:
                best_words.append(word)

        return random.choice(best_words)

    def generate_positional_letter_count(self):
        pass



