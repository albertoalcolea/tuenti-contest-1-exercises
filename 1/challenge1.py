#! /usr/bin/python

import sys
import re


def sum_line(numbers):
    r = 0
    for n in numbers:
        r = r + int(n)
    return r


def parse_line(line):
    return re.findall('[+-]?\d+', line)


def parse_input():
    data = []
    
    for line in sys.stdin:
		data.append(line.split("\n")[0])
        
    return data


# main()
def main():
    data = parse_input()
    for line in data:
        print sum_line(parse_line(line))


if __name__ == '__main__':
    main()
