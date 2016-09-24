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

    with open('data.txt', 'a') as f:
        f.write('{}|{}\n'.format(what, where))


def show_records():

    with open('data.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip().split('|')
            print('{}\t{}'.format(data[0], data[1]))


def main(args):

    if args['add']:
        add_record(args['<what>'], args['<where>'])

    if args['show']:
        show_records()

if __name__ == '__main__':
    args = docopt(__doc__, version='reminder 0.0.1')
    main(args)
