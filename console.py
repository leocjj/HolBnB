#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
    intro = 'AirBnB_clone console.\ngithub users vik407 leocjj\n'
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
    HBNBCommand().cmdloop()
