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


def add_record(what, where):
    print('Chci si uložit {} {}'.format(what, where))


def main(args):

    if args['add']:
        add_record(args['<what>'], args['<where>'])


if __name__ == '__main__':
    args = docopt(__doc__, version='reminder 0.0.1')
    main(args)
