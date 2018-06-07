#!/bin/python
#pylint: disable=too-few-public-methods, missing-docstring, C0413
#-----------------------------------------------------------------------------
# Darkstorm Library
# Copyright (C) 2018 Martin Slater
# Created : Thursday, 07 June 2018 02:56:57 PM
#-----------------------------------------------------------------------------
"""
Scienspeak command line tool.
"""

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from __future__ import absolute_import, print_function
import argparse
import scyli

#-----------------------------------------------------------------------------
# Class
#-----------------------------------------------------------------------------

class Scienspeak(object):
    """ Scienspeak """
    
    def __init__(self, args):
        """ Constructor """
        pass

    def run(self):
        pass

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------

def main():
    """ Main script entry point """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-a', '--arg',
                        help='A boolean arg',
                        dest='barg', action='store_true')
    args = parser.parse_args()
    Scienspeak(args).run()

if __name__ == "__main__":
    main()
