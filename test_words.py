with open('all_words.txt') as file:
    words = [x.strip() for x in file]

words_score = {}
positional_letter_count = {x: {a: 0 for a in "abcdefghijklmnopqrstuvwxyz"} for x in range(5)}

for word in words:
    for i, letter in enumerate(word):
        positional_letter_count[i][letter] += 1

print(positional_letter_count[0])
print(positional_letter_count[1])
print(positional_letter_count[2])
print(positional_letter_count[3])
print(positional_letter_count[4])

def generate_positional_scores():
    for word in words:
        word_score = 0
        for index, letter in enumerate(word):
            word_score += positional_letter_count[index][letter]
        words_score[word] = word_score

generate_positional_scores()

def generate_score(word):
    letters = {x: 0 for x in word}
    print(letters)
    for index, letter in enumerate(word):
        letter_score = positional_letter_count[index][letter]
        if letter_score > letters[letter]:
            letters[letter] = letter_score

    print(letters)
    print(sum(letters.values()))
word_correct = "sores"
print(words_score["sores"])

generate_score(word_correct)