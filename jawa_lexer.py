from sly import Lexer


class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, PRINT, IF,
              ELSE, THEN, EQEQ, FOR, TO, FUN, ARROW}
    ignore = '\t '

    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    # Definisi Token
    PRINT = r'CETAK'
    IF = r'MENAWA'
    ELSE = f'LIYA'
    THEN = r'DENE'
    FOR = r'KANGGO'
    TO = r'TEKAN'
    FUN = r'PUNGSI'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('jawa > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
