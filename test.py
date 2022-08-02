with open("all_words.txt") as file:
    words = [x.strip() for x in file]

letters_count = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
for word in words:
    for letter in set(word):
        letters_count[letter] += 1

words_score = {word: 0 for word in words}

for word in words:
    letters_set = set(word)
    for letter in letters_set:
        words_score[word] += letters_count[letter]

print(letters_count)

best_word = words[0]
for word, value in words_score.items():
    if value > words_score[best_word]:
        best_word = word

def get_hiscore_word(scores, word_list):
    ''' Return the word with the highest score
    use_position: whether or not use position-based scores
    '''

    best_word = ""
    best_score = 0
    for word in word_list:
        if scores[word] > best_score:
            best_score = scores[word]
            best_word = word
    return best_word


def gen_word_scores(word_list):
    letter_count = gen_letter_count(word_list)
    word_scores = {}
    for word in word_list:
        word_score = 0
        for letter in set(list(word)):
            word_score += letter_count[letter]
        word_scores[word] = word_score

    return word_scores

def gen_letter_count(word_list):
    letter_count = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
    for word in word_list:
        for letter in set(word):
            letter_count[letter] += 1

    return letter_count

letter_count = gen_letter_count(words)
word_scores = gen_word_scores(words)

print(max(word_scores, key = lambda key: word_scores[key]))

print(get_hiscore_word(word_scores, words))
print(word_scores["aeros"])
print(word_scores["cares"])


def get_maximized_word(maximized_letters):
    ''' Return the word with maximized number of unique "letters"
    '''
    gen_letter_count(words)
    best_word = ""
    best_score = 0
    for word in words:
        this_score = 0
        for letter in maximized_letters:
            if letter in word:
                this_score += 1
        if this_score > best_score:
            best_score = this_score
            best_word = word
    return best_word