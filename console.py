#!/usr/bin/python3
"""
This module contains the entry point of the command interprete
    for the HBNB program.
"""


import cmd
from models.base_model import BaseModel
from models import storage


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

    def split_arg(self, args):
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        return (class_name, instance_id)

    def do_create(self, arg):
        """
        create: Creates a new instance of BaseModel
            saves it (to the JSON file) and prints the id.
        example: create BaseModel
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] == "BaseModel":
            new_model = BaseModel()
            print(new_model.id)
            new_model.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        example: show BaseModel 1234-1234-1234.
        """
        try:
            class_name, instance_id = self.split_arg(arg.split())
        except TypeError:
            return

        try:
            instance_key = f"{class_name}.{instance_id}"
            instance = storage.all()[instance_key]
        except KeyError:
            print("** no instance found **")
            return
        print(str(instance))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Example: destroy BaseModel 1234-1234-1234
        """
        try:
            class_name, instance_id = self.split_arg(arg.split())
        except TypeError:
            return
        try:
            instance_key = f"{class_name}.{instance_id}"
            del storage.all()[instance_key]
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, arg):
        pass




if __name__ == '__main__':
    HBNBCommand().cmdloop()
