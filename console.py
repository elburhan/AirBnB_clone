#!/usr/bin/python3
"""
This module contains the entry point of the command interprete
    for the HBNB program.
"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Handle EOF (Ctrl+D on Unix, Ctrl+Z on Windows).
        """
        return True




if __name__ == '__main__':
    HBNBCommand().cmdloop()
