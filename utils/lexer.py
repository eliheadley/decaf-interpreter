from enum import Enum, auto

class TokenType(Enum):
    T_AND = auto()
    T_ASSIGN = auto()
    T_BOOLTYPE = auto()
    T_BREAK = auto()
    T_CHARCONSTANT = auto()
    T_COMMA = auto()
    T_COMMENT = auto()
    T_CONTINUE = auto()
    T_DIV = auto()
    T_DOT = auto()
    T_ELSE = auto()
    T_EQ = auto()
    T_EXTERN = auto()
    T_FALSE = auto()
    T_FOR = auto()
    T_FUNC = auto()
    T_GEQ = auto()
    T_GT = auto()
    T_ID = auto()
    T_IF = auto()
    T_INTCONSTANT = auto()
    T_INTTYPE = auto()
    T_LCB = auto()
    T_LEFTSHIFT = auto()
    T_LEQ = auto()
    T_LPAREN = auto()
    T_LSB = auto()
    T_LT = auto()
    T_MINUS = auto()
    T_MOD = auto()
    T_MULT = auto()
    T_NEQ = auto()
    T_NOT = auto()
    T_NULL = auto()
    T_OR = auto()
    T_PACKAGE = auto()
    T_PLUS = auto()
    T_RCB = auto()
    T_RETURN = auto()
    T_RIGHTSHIFT = auto()
    T_RPAREN = auto()
    T_RSB = auto()
    T_SEMICOLON = auto()
    T_STRINGCONSTANT = auto()
    T_STRINGTYPE = auto()
    T_TRUE = auto()
    T_VAR = auto()
    T_VOID = auto()
    T_WHILE = auto()
    T_WHITESPACE = auto()
    UNKNOWN = auto()
    

class Token:
    def __init__(self, token_type: TokenType, lexeme: str, line: int, col: int):
        self.token_type = token_type
        self.lexeme = lexeme      
        self.line = line
        self.col = col

    def __repr__(self):
        return f"Token({self.token_type.name}, {self.lexeme!r}, line={self.line}, col={self.col})"


class Lexer:
    keywords = {
        "bool":     TokenType.T_BOOLTYPE,
        "break":    TokenType.T_BREAK,
        "continue": TokenType.T_CONTINUE,
        "else":     TokenType.T_ELSE,
        "extern":   TokenType.T_EXTERN,
        "false":    TokenType.T_FALSE,
        "for":      TokenType.T_FOR,
        "func":     TokenType.T_FUNC,
        "if":       TokenType.T_IF,
        "int":      TokenType.T_INTTYPE,
        "null":     TokenType.T_NULL,
        "package":  TokenType.T_PACKAGE,
        "return":   TokenType.T_RETURN,
        "string":   TokenType.T_STRINGTYPE,
        "true":     TokenType.T_TRUE,
        "var":      TokenType.T_VAR,
        "void":     TokenType.T_VOID,
        "while":    TokenType.T_WHILE,
    }

    operators = {
        "&&":  TokenType.T_AND,
        "||":  TokenType.T_OR,
        "==":  TokenType.T_EQ,
        "!=":  TokenType.T_NEQ,
        ">=":  TokenType.T_GEQ,
        "<=":  TokenType.T_LEQ,
        "<<":  TokenType.T_LEFTSHIFT,
        ">>":  TokenType.T_RIGHTSHIFT,
        "=":   TokenType.T_ASSIGN,
        ">":   TokenType.T_GT,
        "<":   TokenType.T_LT,
        "+":   TokenType.T_PLUS,
        "-":   TokenType.T_MINUS,
        "*":   TokenType.T_MULT,
        "/":   TokenType.T_DIV,
        "%":   TokenType.T_MOD,
        "!":   TokenType.T_NOT,
    }

    punctuation = {
        "{":  TokenType.T_LCB,
        "}":  TokenType.T_RCB,
        "(":  TokenType.T_LPAREN,
        ")":  TokenType.T_RPAREN,
        "[":  TokenType.T_LSB,
        "]":  TokenType.T_RSB,
        ";":  TokenType.T_SEMICOLON,
        ",":  TokenType.T_COMMA,
        ".":  TokenType.T_DOT,
    }

    def tokenize(self, source_code: str) -> Token:
        lines = source_code.split('\n')
        print(lines)