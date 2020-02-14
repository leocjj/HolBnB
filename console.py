#!/usr/bin/python3
""" Console module. Used for user command line intructions."""

import cmd, sys

class HBNBCommand(cmd.Cmd):
    intro = '\n..............................\n'\
            '. AirBnB_clone console V0.1  .\n'\
            '. For help type: help        .\n'\
            '..............................\n'\
            '. github users vik407 leocjj .\n'\
            '..............................\n'
    prompt = '(hbnb) '
    file = None

    # ----- basic turtle commands -----
    def do_quit(self, arg):
        'Quit the program!'
        exit(0)
    def do_EOF(self, arg):
        'Quit the program!'
        exit(0)
    def emptyline(self):
        'Do nothing if empty line is entered!'
        pass
    def default(self, arg):
        'Do nothing if wrong command is entered!'
        pass

#def parse(arg):
#    'Convert a series of zero or more numbers to an argument tuple'
#    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    while True:
        try:
            HBNBCommand().cmdloop()
        except KeyboardInterrupt:
            continue
