from util import readJSON, findAndReplace
from ipa import numbersIPA, changeToIPA, transformSentence, ipaToWords
from downloadJSON import downloadIPAJson
from os.path import exists


def main():
    if not exists("IPA.json"):
        downloadIPAJson()

    ipaJSON = readJSON("IPA.json")
    ipaNumbers = numbersIPA(ipaJSON)
    sentence = input("Enter a sentence: ")
    ipaSentence = changeToIPA(ipaJSON, sentence)
    # print(ipaSentence)
    transformedSentence = transformSentence(ipaNumbers, ipaSentence)
    # print(transformedSentence)
    findAndReplace = findAndReplace(ipaSentence, transformedSentence)
    # print(findAndReplace)
    print((sentence, ipaSentence, findAndReplace))
    finalSentence = ipaToWords(sentence, ipaSentence, findAndReplace)
    print(finalSentence)
    print(" ".join(x for x in finalSentence))


if __name__ == "__main__":
    main()
