from translate import *
with open('D:/ZeroToMasteryPython/File Input Output in Python/Translate.txt',mode='r') as my_file:
    #print(my_file.readlines())
    translator = Translator(to_lang="de")
    c = my_file.read()

    print(translator.translate(c))