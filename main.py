import jawa_lexer
import jawa_parser
import jawa_interpreter

from sys import *

# DENGAN MASUKAN BAHASAKU.RHS
lexer = jawa_lexer.BasicLexer()
parser = jawa_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    jawa_interpreter.BasicExecute(tree, env)
