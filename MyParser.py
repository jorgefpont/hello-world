# nand2tetris
# first iteration of a parser
# used for assembler
# both files must exist
# filemanes entered in quotations: eg:
# filter('test_text_file.txt', 'test_text_file_new.txt')


def filter(infile, newfile):

    f1 = open(infile, 'r')
    f2 = open(newfile, 'w')
    
    while True:
        text = f1.readline()

        # left align
        text = text.lstrip()

        print(text)
        
        if text == "":
           break
        if text[0] == '/':
           continue
        f2.write(text)

    f1.close()
    f2.close()
    return

infile = 'Mult.txt'
filter(infile, 'NewMult.txt')
