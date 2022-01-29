import PreProcessData.TrectextCollection as TrectextCollection
import PreProcessData.TrecwebCollection as TrecwebCollection
import PreProcessData.StopWordRemover as StopWordRemover
import PreProcessData.WordNormalizer as WordNormalizer
import PreProcessData.WordTokenizer as WordTokenizer
import Classes.Path as Path
import datetime

# !!! YOU CANNOT CHANGE ANYTHING IN THIS CLASS !!! This is for INFSCI 2140 in
# Fall 2021


def PreProcess(type):
    # Open the collection by type.
    if type == "trectext":
        collection = TrectextCollection.TrectextCollection()
    else:
        collection = TrecwebCollection.TrecwebCollection()

    # Initialize essential objects.
    stopwordRemover = StopWordRemover.StopWordRemover()
    normalizer = WordNormalizer.WordNormalizer()
    wr = open(Path.ResultHM1 + type, "w", encoding="utf8")
    doc = []

    # Process the corpus, document by document, iteratively.
    count = 0
    while True:
        doc = collection.nextDocument()

        # BEN EDIT: correct "None" comparison
        # if doc == None:
        if doc is None:
            break
        docNo = doc[0]
        content = doc[1]

        # Output the docNo.
        wr.write(docNo+"\n")

        # Output the preprocessed content.
        tokenizer = WordTokenizer.WordTokenizer(content)

        while True:
            word = tokenizer.nextWord()
            if word == None:
                break
            word = normalizer.lowercase(word)

            # BEN EDIT clarify boolean comparison
            # if stopwordRemover.isStopword(word) == False:
            if not stopwordRemover.isStopword(word):
                wr.write(normalizer.stem(word) + " ")

        wr.write("\n")
        count += 1

        if count % 10000 == 0:
            # BEN EDIT: this is an illegal string/int concatenation in python 3
            # print("finish " + count + " docs")
            print(f"finished {count} docs")
            setstart = datetime.datetime.now()
    wr.close()
    return


startTime = datetime.datetime.now()
PreProcess("trectext")
endTime = datetime.datetime.now()
# BEN EDIT: clarify which corpus produced this runtime
print("index TEXT corpus running time: ", endTime - startTime)

startTime = datetime.datetime.now()
PreProcess("trecweb")
endTime = datetime.datetime.now()
# BEN EDIT: clarify which corpus produced this runtime
print("index WEB corpus running time: ", endTime - startTime)
