#!/usr/bin/env python3

import re

def mad_lib(input_file, output_file):
    """Reads text file and lets user substitute text whenver the word ADJECTIVE, NOUN, ADVERB, or VERB appears 
       Case sensitive - mad lib words must be in CAPS
    Args:
        input_file (string): name of input file to be read from
        output_file (string): name of output file to be written into
    Returns:
        None

    Outputs substituted mad lib text into output_file
    """

    madlib_regx = re.compile(r'(ADJECTIVE|NOUN|VERB|ADVERB)')

    text_file = open(input_file, 'r')
    contents = text_file.read()

    matches = madlib_regx.findall(contents)

    for word in matches:
        if word == 'ADJECTIVE':
            substitute = input(f'Enter an {word.upper()}: ')
        else:
            substitute = input(f'Enter a {word.upper()}: ')
        contents = contents.replace(word, substitute, 1)
    
    o_file = open(output_file, 'w')
    o_file.write(contents)


if __name__ == '__main__':
    mad_lib('input.txt', 'output.txt')
