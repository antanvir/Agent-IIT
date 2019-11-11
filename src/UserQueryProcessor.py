import difflib
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import Utility


global spell, ps, stop_words
global myKeywords, extractKeywords, withoutStopTokenizedWords, closeMatched


stemmedWords = []
correctedWords = []
suggestedWords = []
extractKeywords = []
closeMatched = []
withoutStopTokenizedWords = []
# myKeywords = ['2nd','4th','6th','8th','exam','xm','2','4','6','8','o+','a+','b+','o-','a-','b-','iit', 'class', 'routine' ,
#              'student' , 'teacher' , 'course' , 'faculty' , 'blood' ,'semester', 'when','what', 'who', 'tomorrow', 'today', ]

myKeywords = ['exam', 'xm', 'o+', 'a+', 'b+', 'o-', 'a-', 'b-', 'iit', 'class', 'routine', 'student', 'teacher', 'course', 'rifat',
        'faculty', 'blood', 'semester', 'when', 'what', 'who', 'tomorrow', 'today', 'next', 'hi', 'hello', 'bye', 'time', 'faculty',
        'okay', 'thanks', 'thank', 'ok', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'shariful', 'islam', 'zerina', 'begum',
        'zulfiquar', 'hafiz', 'mahbubul', 'joarder', 'kazi', 'sakib', 'muheymin', 'muheymin-us-sakib', 'mohommad', 'shoyaib', 'shafiul',
        'khan', 'mainul', 'hossain', 'naushin', 'nower', 'ahmedul', 'kabir', 'nurul', 'ahad', 'tawhid', 'saeed', 'siddik', 'nadia',
        'nahar', 'abdus', 'sattar', 'kishan', 'kumar', 'ganguly', 'poddar', 'iftekharul', 'mahbubur', 'shariat', 'shahdad', 'distributed',
        'mis', 'management', 'ethics', 'artificial', 'intelligence', 'ai', 'testing', 'assurance', 'design', 'analysis', 'metrics', 'ml',
        'machine', 'project', 'network', 'security', 'specification', 'requirements', 'srs', 'bus', 'business', 'dbms', 'database', 'db',
        'psychology', 'operating', 'os', '9th', '9', '6', '6th', '10th', '10', '4', '4th', '8th', '8', '11th', '11', '2', '2nd']


def initialize(): 
    global spell, ps, stop_words, myKeywords
    #example_sent = input()
    spell = SpellChecker()
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    # print(myKeywords)
    # myKeywords.extend(Utility.greetings.keys())
    # myKeywords.extend(Utility.dayName.keys())
    # myKeywords.extend(Utility.teacher_Id.keys())
    # myKeywords.extend(Utility.course.keys())
    # myKeywords.extend(Utility.semester.keys())



def process(userInput):
    global myKeywords, extractKeywords, withoutStopTokenizedWords, closeMatched

    stemmedWords = []
    correctedWords = []
    suggestedWords = []
    extractKeywords = []
    closeMatched = []
    withoutStopTokenizedWords = []

    userInput = userInput.lower()
    tokenizedWords = word_tokenize(userInput)
    # print(tokenizedWords)

    for word in tokenizedWords:
        if word in myKeywords:
            extractKeywords.append(word)
            tokenizedWords.remove(word)

    for word in tokenizedWords:
        if word not in stop_words:
            withoutStopTokenizedWords.append(word)

    for word in withoutStopTokenizedWords:
        temp = []
        temp = difflib.get_close_matches(word, myKeywords)
        if  temp:
            closeMatched.append(temp)

    for wordlist in closeMatched:
        for word in wordlist:
            if word in myKeywords and word not in extractKeywords:
                extractKeywords.append(word)

    return extractKeywords

    # misSpelled = spell.unknown(withoutStopTokenizedWords)
    # for word in misSpelled:
    #     correctedWords.append(spell.correction(word))
    #     suggestedWords.append(spell.candidates(word))

    # for word in correctedWords:
    #         if word in myKeywords and word not in extractKeywords:
    #             extractKeywords.append(word)


    # for word  in withoutStopTokenizedWords:
    #     stemmedWords.append(ps.stem(word))

    # for word in stemmedWords:
    #         if word in myKeywords and word not in extractKeywords:
    #             extractKeywords.append(word)

    # if len(extractKeywords) < 2:
    #     for word in suggestedWords:
    #         if word in myKeywords and word not in extractKeywords:
    #             extractKeywords.append(word)



def main():
    initialize()
    while True:
        line = input()
        if line != "q":
            extractKeywords = process(line)
            print(extractKeywords)
            # roots = findRoots(word_tokens)
        else:
            break


if __name__ == "__main__":
    main()