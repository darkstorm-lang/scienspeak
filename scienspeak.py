#!/bin/python
#pylint: disable=too-few-public-methods, missing-docstring, C0413
#-----------------------------------------------------------------------------
# Darkstorm Library
# Copyright (C) 2018 Martin Slater
# Created : Thursday, 07 June 2018 02:56:57 PM
#-----------------------------------------------------------------------------
"""
Tool for generating a plausible way of pronouncing scientific names. The way will
probably be wrong but as many point out most pronunciations are anyway, but at
least you will have some conistency to your wrongness. Given a word (or series of words)
on the command line it will output them punctuated into individual syllables with the
syllable that should receive the stress in capitals.
"""

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from __future__ import absolute_import, print_function
import argparse
import sys
import sylli

#-----------------------------------------------------------------------------
# Class
#-----------------------------------------------------------------------------
class Scienspeak(object):
    """ Scienspeak """

    def __init__(self, args):
        """ Constructor """
        pass

    def run(self, name):
        # convert 'ae' digraph to an 'e' otherwise the syllabliser will get confused.
        # in latin it is a single vowel.
        words = name.replace('ae', 'e')
        self.words = [ word.strip().lower() for word in words.split(' ') ]

        syl = sylli.SylModule()
        result = ''
        for word in self.words:
            # split into individual syllables
            syllables = syl.syllabify(word).split('.')
            final = []

            #-----------------------------------------------------------------------------
            # Stressing rules for syllables
            #-----------------------------------------------------------------------------
            # == 1 -> Stress on it
            # == 2 -> Stress on first syllable, sound s short vowel if followed by 2 consonants
            # >= 2 -> IF second to last syllable is followed by 2 consonants
            #         OR the vowel is long (?)
            #         THEN stress second to last syllable
            #         ELSE stress third to last syllable
            #-----------------------------------------------------------------------------
            if len(syllables) == 1:
                final.append(syllables[0].upper())
            elif len(syllables) == 2:
                final.append(syllables[0].upper())
                final.append(syllables[1])
            else:
                #TODO: how to tell if it is a long vowel with a macron that is used to indicate it
                #      we just use 2nd to last for now
                num_syllables = len(syllables)
                for idx in range(num_syllables):
                    cur = syllables[idx]
                    if idx == (num_syllables-2):
                        final.append(cur.upper())
                    else:
                        final.append(cur)

            result += '.'.join(final) + ' '

        return result

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------

def main():
    """ Main script entry point """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--file', '-f', dest='file_input', action='store_true',
                        help='Read input from file with one entry per line')
    parser.add_argument('positional_args', nargs='+')
    args = parser.parse_args()
    temp_names = []
    if args.file_input:
        with open(args.positional_args[0]) as ifile:
            temp_names = ifile.readlines()
    else:
        temp_names.append(args.positional_args[0])

    # strip whitespace and find longest string for pretty output
    max_len = -1
    input_names = []
    for name in temp_names:
        name = name.strip()
        if len(name) > max_len:
            max_len = len(name)
        input_names.append(name)

    output_names = []
    max_out_len = -1
    for name in input_names:
        res = Scienspeak(args).run(name)
        if len(res) > max_out_len:
            max_out_len = len(res)
        output_names.append(res)

    full_width = max_out_len + max_len + 7
    for iname, oname in zip(input_names, output_names):
        print('-' * full_width)
        print(str.format('| {0: <{width}} | {1: <{width2}} |', iname, oname, width=max_len, width2=max_out_len))
    print('-' * full_width)

if __name__ == "__main__":
    main()
