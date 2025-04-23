#include <stdio.h>
#include <string.h>
#include <ctype.h>

const char* keywords[] = {"int", "float", "if", "else", "return"};
const int num_keywords = 5;

int is_keyword(const char* str) {
    for (int i = 0; i < num_keywords; i++) {
        if (strcmp(str, keywords[i]) == 0)
            return 1;
    }
    return 0;
}

int is_operator(char ch) {
    return strchr("+-*/=<>", ch) != NULL;
}

int is_punctuation(char ch) {
    return strchr(";(){}", ch) != NULL;
}

void tokenize(const char* code) {
    char token[100];
    int i = 0, j;

    while (code[i]) {
        if (isspace(code[i])) {
            i++;
            continue;
        }

        if (isalpha(code[i])) {
            j = 0;
            while (isalnum(code[i])) {
                token[j++] = code[i++];
            }
            token[j] = '\0';
            if (is_keyword(token))
                printf("<KEYWORD, %s>\n", token);
            else
                printf("<IDENTIFIER, %s>\n", token);
        }
        else if (isdigit(code[i])) {
            j = 0;
            while (isdigit(code[i])) {
                token[j++] = code[i++];
            }
            token[j] = '\0';
            printf("<NUMBER, %s>\n", token);
        }
        else if (is_operator(code[i])) {
            printf("<OPERATOR, %c>\n", code[i++]);
        }
        else if (is_punctuation(code[i])) {
            printf("<PUNCTUATION, %c>\n", code[i++]);
        }
        else {
            printf("<UNKNOWN, %c>\n", code[i++]);
        }
    }
}

int main() {
    char line[256];
    printf("Enter code: ");
    fgets(line, sizeof(line), stdin);
    tokenize(line);
    return 0;
}
