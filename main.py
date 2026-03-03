import argparse
from utils.lexer import TokenType, Token, Lexer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, default="./test/t1.decaf", help="Source file path")
    args = parser.parse_args()

    with open(args.source, "r") as file:
        source_code = file.read()

    lexer = Lexer()
    lexer.tokenize(source_code)

if __name__ == "__main__":
    main()