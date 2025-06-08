# Henry Huitema
# This program searches through a user-supplied message and checks it against a list of 30 phrases
# commonly found in spam emails. It then returns spam score (number of phrases found),
# the specific phrases found, and an estimate of how likely the message is to be spam based on the spam score.

def countPhrases(message):
    phraseList = ["act now", "free gift", "free money", "once in a lifetime", "call now", "apply now",
                  "instant", "limited time", "great deal", "amazing deal", "prize", "winner", "join millions",
                  "urgent", "extra cash", "be your own boss", "double your cash", "double your income",
                  "guaranteed", "free access", "risk free", "pure profit", "no fees", "no hidden cost",
                  "not junk", "not spam", "not a scam", "become debt free", "cash bonus", "buy now"]
    phrasesAndCounts = {}
    # Store the output of message.lower() to allow for case-insensitive checks.
    # "Buy now", "buy now", and "BUY NOW" all increase the spam score.
    messageLower = message.lower()
    # Iterate over phraseList, checking each phrase against the message.
    for phrase in phraseList:
        # Only add the phrase and frequency in as a key value pair if the phrase actually shows up.
        if phrase in messageLower:
            phrasesAndCounts[phrase] = messageLower.count(phrase)
    return phrasesAndCounts

def getScore(phrasesFound):
    # Initialize score
    score = 0
    # Take the values of the dictionary returned by countPhrases, convert it to a list,
    # and iterate over it to get the sum.
    for i in list(phrasesFound.values()):
        score += i
    return score

def getPhrases(phrasesFound):
    # Take the keys of the dictionary returned, convert it to a list, and return it
    phrasesInMessage = list(phrasesFound.keys())
    return phrasesInMessage

def rateMessage(score):
    # I wasn't too sure how to find the probability, but I decided on the following curve:
    # The function returns a percentage probability, clamped between 0% and 100%. It first takes the raw
    # spam score (number of phrases found) and returns the raw score minus 1 and times 20, or 0% if that
    # is a negative value (0 or 1 hits). It then returns that value or 100%, whichever is lower. The expected
    # output based on the raw score is: 1 or less = 0%, 2 = 20%, 3 = 40%, 4 = 60%, 5 = 80%, 6 or more = 100%
    percentFloored = max((score - 1) * 20, 0)
    return min(percentFloored, 100)

def main():
    hits = countPhrases(input("Please input the contents of an email: "))
    print(f"\nThe email has a spam score of {getScore(hits)}.")
    print(f"This is because it contains the following phrases: {getPhrases(hits)}.")
    print(f"The program believes there's a {rateMessage(getScore(hits))}% chance the message is spam.")
if __name__ == "__main__":
    main()
