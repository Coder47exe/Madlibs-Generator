with open("story.txt","r") as f:                               # created a txt file to read a story
    story = f.read()

words = set()                                                  # creating set 'words' to store words from story
start_of_word = -1

target_start = "<"
target_end = ">"


for i, char in enumerate(story):                               # for loop to enumerate the story
    if char == target_start:                                   # used condition to start counting of  words from 0 index
        start_of_word = i

    if char == target_end and start_of_word!= -1:              # used condition to stop counting of words
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}                                                   # creating dictionary

for word in words:                                             # to get word from set words
    answer = input("Enter a word for " + word +":")
    answers[word] = answer

for word in words:
    story = story.replace(word,answers[word])                  # replacing those words with user input

print(story)


