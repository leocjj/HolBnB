#!/usr/bin/python3
""" Console module. Used for user command line intructions."""

import cmd, sys, models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    intro = '\n..............................\n'\
            '. AirBnB_clone console V0.1  .\n'\
            '. For help type: help        .\n'\
            '..............................\n'\
            '. github users vik407 leocjj .\n'\
            '..............................\n'
    prompt = '(hbnb) '
    file = None

    # ----- basic commands -----
    def do_create(self, arg):
        'Create new instance, saves it (to JSON file) and prints the id.\n'\
        'Usage: create <class_name>\n'
        if arg == '':
            print('** class name missing **')
            return
        args = arg.split()
        try:
            new_instance = eval(args[0] + '()')
            print(new_instance.id)
            new_instance.save()
        except:
            print("** class doesn't exist **")
            return
    def do_quit(self, arg):
        'Quit the program!'
        exit(0)
    def do_EOF(self, arg):
        'Quit the program!'
        print()
        exit(0)
    def emptyline(self):
        'Do nothing if empty line is entered!'
        pass
    def default(self, arg):
        'Do nothing if wrong command is entered!'
        pass

#def parse(arg):
#    'Convert arguments string to an arguments list'
#    return list(map(int, arg.split()))

if __name__ == '__main__':
    while True:
        try:
            HBNBCommand().cmdloop()
        except KeyboardInterrupt:
            continue
