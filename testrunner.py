words = ['eerie']


letters_count = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}
for word in words:
    for letter in set(word):
        letters_count[letter] += 1

words_scores = {word: 0 for word in words}


for word in words:
    word_score = 0
    for letter in set(word):
        word_score += letters_count[letter]
    words_scores[word] = word_score

maximum = max(words_scores.values())
table = []
for word, score, in words_scores.items():
    if score == maximum:
        table.append(word)

print(words_scores)
