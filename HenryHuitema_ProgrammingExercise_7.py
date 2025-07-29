# Henry Huitema
# This program prompts the user to input a paragraph of text and uses regex to
# find each individual sentence in the paragraph. It then prints each sentence
# one by one and displays the number of sentences found in the paragraph.

import re

def getSentences(paragraph):
    # This pattern matches any number of characters preceding a period, question mark, or exclamation point.
    pattern = r'.*?[.?!]'
    return re.findall(pattern, paragraph)

def main():
    userInput = input("Enter a paragraph of text: ")
    sentences = getSentences(userInput)
    sentenceCount = 0
    for s in sentences:
        sentenceCount = sentenceCount + 1
        print(s)
    print(f"There are {sentenceCount} sentences.")

if __name__ == "__main__":
    main()