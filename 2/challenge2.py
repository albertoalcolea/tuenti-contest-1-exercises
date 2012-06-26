#! /usr/bin/python

import sys
import re


def expr(tokens):
    reconocer(tokens, '^')
    n1 = operador(tokens)
    reconocer(tokens, '$')
    return n1
    
    
def operador(tokens):
    if   (tokens[0] == '='): return suma(tokens)
    elif (tokens[0] == '#'): return mult(tokens)
    elif (tokens[0] == '@'): return resta(tokens)
    

def suma(tokens):
    reconocer(tokens, '=')
    n1 = elem(tokens)
    n2 = elem(tokens)
    return n1 + n2
    
    
def mult(tokens):
    reconocer(tokens, '#')
    n1 = elem(tokens)
    n2 = elem(tokens)
    return n1 * n2
    

def resta(tokens):
    reconocer(tokens, '@')
    n1 = elem(tokens)
    if tokens[0] != '$':
        n2 = elem(tokens)
        return n1 - n2
    else:
        return -n1
    
    
def elem(tokens):
    if tokens[0].isdigit():
        return int(tokens.pop(0))
    elif tokens[0] == '^':
        return expr(tokens);        
    
    
def reconocer(tokens, token):
    if token == tokens[0]:
        tokens.pop(0)



def parse_line(line):
    line_parsed = re.findall('\^|=|#|@|\$|\d+', line)
    return line_parsed



def parse_input():
    data = []
    
    for line in sys.stdin:
		data.append(line.split("\n")[0])
        
    return data


# main()
def main():
    data = parse_input()
    for line in data:
        line_tokens = parse_line(line)
        print expr(line_tokens)


if __name__ == '__main__':
    main()
