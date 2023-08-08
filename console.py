#!/usr/bin/python3
""" This module contains HBNB CLI Interpreter """
from cmd import Cmd


class HBNBCommand(Cmd):
    """
    Class representing the hbnb CLI.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Exits the console """
        return True

    def help_quit(self):
        """ Quit Command Help """
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """ End of line marker """
        print()
        return True

    def emptyline(self):
        """ Ignore empty lines """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
