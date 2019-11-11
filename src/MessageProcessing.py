from spellchecker import SpellChecker
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer


global spell, ps, stop_words


def initialize(): 
    global spell, ps, stop_words
    #example_sent = input()
    spell = SpellChecker()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))


def tokenizeMessage(message):
    word_tokens = word_tokenize(message)
    print("Tokenized word => ",word_tokens)
    return word_tokens

    # filtered_sentence = [w for w in word_tokens if not w in stop_words]
    # filtered_sentence = []
    # for w in word_tokens:
    #     if w not in stop_words:
    #         filtered_sentence.append(w)
    # print("tokenized words => ",filtered_sentence)
    # suggestedWords = []
    # misspelled = spell.unknown(filtered_sentence)
    # print("Misspelled words--",misspelled)
    # for word in filtered_sentence:
    #     if word in misspelled:
    #         filtered_sentence.remove(word)


    # for word in misspelled:
    #     print("most likely word--",spell.correction(word))
    #     filtered_sentence.append(spell.correction(word))
    #     print("Suggested words--",spell.candidates(word))
    #     suggestedWords.append(spell.candidates(word))


def findRoots(tokens): 
    global ps
    rootWords = []
    print("Roots of the words:\n--------------------")
    for word in tokens:
        print(word, " : ", ps.stem(word))
        rootWords.append(ps.stem(word))

    print("Word roots => ",rootWords)
    # print("Suggested words for missplelled words--",suggestedWords)
    return rootWords


def main():
    initialize()
    while True:
        line = input()
        if line != "q":
            word_tokens = tokenizeMessage(line)
            roots = findRoots(word_tokens)
        else:
            break


if __name__ == "__main__":
    main()