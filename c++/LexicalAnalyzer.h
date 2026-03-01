#ifndef LEXICAL_ANALYZER_H
#define LEXICAL_ANALYZER_H

#include <string>
#include <unordered_map>
#include <vector>

enum TokenType {
    T_AND,              // &&
    T_ASSIGN,           // =
    T_BOOLTYPE,         // bool
    T_BREAK,            // break
    T_CHARCONSTANT,     // char_lit (character literal)
    T_COMMA,            // ,
    T_COMMENT,          // comment
    T_CONTINUE,         // continue
    T_DIV,              // /
    T_DOT,              // .
    T_ELSE,             // else
    T_EQ,               // ==
    T_EXTERN,           // extern
    T_FALSE,            // false
    T_FOR,              // for
    T_FUNC,             // func
    T_GEQ,              // >=
    T_GT,               // >
    T_ID,               // identifier
    T_IF,               // if
    T_INTCONSTANT,      // int_lit (integer literal)
    T_INTTYPE,          // int
    T_LCB,              // {
    T_LEFTSHIFT,        // <<
    T_LEQ,              // <=
    T_LPAREN,           // (
    T_LSB,              // [
    T_LT,               // <
    T_MINUS,            // -
    T_MOD,              // %
    T_MULT,             // *
    T_NEQ,              // !=
    T_NOT,              // !
    T_NULL,             // null
    T_OR,               // ||
    T_PACKAGE,          // package
    T_PLUS,             // +
    T_RCB,              // }
    T_RETURN,           // return
    T_RIGHTSHIFT,       // >>
    T_RPAREN,           // )
    T_RSB,              // ]
    T_SEMICOLON,        // ;
    T_STRINGCONSTANT,   // string_lit (string literal)
    T_STRINGTYPE,       // string
    T_TRUE,             // true
    T_VAR,              // var
    T_VOID,             // void
    T_WHILE,            // while
    T_WHITESPACE,       // whitespace
    Unknown
};

class LexicalAnalyzer{
    private:
        std::unordered_map<std::string, TokenType> keywords;
        std::unordered_map<std::string, TokenType> operators;
        std::unordered_map<std::string, TokenType> punctuation;

        void initKeywords();
        void initOperators();
        void initPunctuation();
        bool isWhiteSpace(char c);
        bool isLetter(char c);
        bool isDigit(char c);
        bool isPunctuation(char c);
        bool isOperator(char c);
        void removeComments(std::string* input);
        int getColumnEnd(int col, std::string token);
        std::string getNextWord(int* position, std::string* text, int* line, int* col);
        std::string getType(TokenType type);

    public:
        LexicalAnalyzer(std::string* source);
        void tokenize();
        void printTokens();
};

#endif