#!/usr/bin/python3
""" Console module. Used for user command line intructions."""

import cmd, sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Console class. Used for user command line intructions."""

    intro = '\n..............................\n'\
            '. AirBnB_clone console V0.1  .\n'\
            '. For help type: help        .\n'\
            '..............................\n'\
            '. github users vik407 leocjj .\n'\
            '..............................\n'
    prompt = '(hbnb) '
    HBNBCommand_classes = ['BaseModel']
    file = None

    def do_create(self, line):
        '\nCreate new instance, saves it (to JSON file) and prints the id.\n'\
        '-> Usage: (hbnb) create <class_name>\n'
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if len(args) == 1:
            try:
                new_instance = eval(args[0] + '()')
                new_instance.save()
                print(new_instance.id)
            except:
                print("** class doesn't exist **")
                return
        else:
            print('** class name missing **')
            return

    def do_show(self, line):
        '\nPrints string representation of an instance.\n'\
        '-> Usage: (hbnb) show <class_name> <id>\n'
        if not line:
            print('** class name missing **')
            return

        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        if args[0] not in self.HBNBCommand_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            try:
                print(storage.all()[args[0] + '.' + args[1]])
            except KeyError:
                print("** no instance found **")
                return

    def do_destroy(self, line):
        '\nDeletes an instance based on the class name and id.\n'\
        '-> Usage: (hbnb) destroy <class_name> <id>\n'
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        if args[0] not in self.HBNBCommand_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            try:
                del storage.all()[args[0] + '.' + args[1]]
            except KeyError:
                print("** no instance found **")
                return

    def do_all(self, line):
        '\nPrints all string representation of all instances based or not on\n'
        'the class name.\n'\
        '-> Usage: (hbnb) all <class_name>\n'
        '-> Usage: (hbnb) all\n'
        if not line:
            a = []
            for key, value in storage.all().items():
                a.append(str(value))
            print(a)
            return
        args = line.split()
        if len(args) == 1:
            if args[0] not in self.HBNBCommand_classes:
                print("** class doesn't exist **")
                return
            a = []
            for key, value in storage.all().items():
                if str(key.split('.')[0]) == args[0]:
                    a.append(str(value))
            print(a)
            return

    def do_update(self, line):
        '\nDeletes an instance based on the class name and id.\n'\
        '-> Usage: (hbnb) destroy <class_name> <id>\n'
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        if len(args) >= 1 and args[0] not in self.HBNBCommand_classes:
                print("** class doesn't exist **")
                return
        if len(args) == 1:
            print('** instance id missing **')
            return
        if len(args) >=2:
            try:
                storage.all()[args[0] + '.' + args[1]]
            except KeyError:
                print("** no instance found **")
                return
        if len(args) == 2:
            print('** attribute name missing **')
            return
        if len(args) == 3:
            print('** value missing **')
            return
        if len(args) == 4:
            try:
                try:
                    if '.' in args[3]:
                        value = float(args[3])
                    else:
                        value = int(args[3])
                except ValueError:
                    value = str(args[3]).strip("\"':")
                setattr(storage.all()[args[0] + '.' + args[1]], args[2].strip("\"':"), value)
                storage.save()
            except KeyError:
                print("** no instance found **")
                return


    def do_quit(self, line):
        'Quit the program!'
        exit(0)
    def do_EOF(self, line):
        'Quit the program!'
        print()
        exit(0)
    def emptyline(self):
        'Do nothing if empty line is entered!'
        pass
    def default(self, line):
        'Do nothing if wrong command is entered!'
        pass

#def parse(line):
#    'Convert arguments string to an arguments list'
#    return list(map(int, line.split()))

if __name__ == '__main__':
    while True:
        try:
            HBNBCommand().cmdloop()
        except KeyboardInterrupt:
            continue
