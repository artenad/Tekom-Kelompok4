import jawa_lexer
import jawa_parser
import jawa_interpreter

from sys import *

# MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = jawa_lexer.BasicLexer()
    parser = jawa_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('jawa > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            jawa_interpreter.BasicExecute(tree, env)
