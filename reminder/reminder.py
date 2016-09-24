#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Reminder.

Usage:
  reminder show
  reminder add <what> <where>
  reminder -h | --help
  reminder --version

Options:
  -h --help     Show this screen.
  --version     Show version.
'''

from docopt import docopt


def main(args):
    print("Ted už pracuju")
    print(args)
    pass


if __name__ == '__main__':
    args = docopt(__doc__, version='reminder 0.0.1')
    main(args)
