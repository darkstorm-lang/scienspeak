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
        # convert 'ae' digraph to an 'e' otherwise the syllabliser will get confused.
        # in latin it is a single vowel.
        words = args.words[0].replace('ae', 'e')

        self.words = [ word.strip().lower() for word in words.split(' ') ]

    def run(self):
        syl = sylli.SylModule()
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

            sys.stdout.write('.'.join(final) + ' ')


#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------

def main():
    """ Main script entry point """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('words', nargs='+')
    args = parser.parse_args()
    Scienspeak(args).run()

if __name__ == "__main__":
    main()
