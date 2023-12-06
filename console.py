#!/usr/bin/python3
"""
This module contains the entry point of the command interprete
    for the HBNB program.
"""


import cmd
from models.base_model import BaseModel
from models import storage
import re


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
        if class_name not in storage.classes():
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

        if args[0] in storage.classes():
            new_model = storage.classes()[args[0]]()
            print(new_model.id)
            new_model.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        example: show BaseModel 1234-1234-1234.
        """
        args = arg.split()
        try:
            class_name, instance_id = self.split_arg(args)
        except TypeError:
            return

        try:
            instance_key = f"{class_name}.{instance_id}"
            instance = storage.all()[instance_key]
        except KeyError:
            print("** no instance found **")
            return
        print(instance)

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
        """
        Prints all string representation of all instances based or not on the class name.
        Example: all BaseMode
        or
        all.
        """
        if arg:
            args = arg.split()

            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return

            new_list = [str(obj) for k, v in storage.all().items()
                        if type(obj).__name__ == args[0]]
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
        
        if not new_list:
            return
        print(new_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        Example: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, arg)
        class_name = match.group(1)
        instance_id = match.group(2)
        attribute_name = match.group(3)
        attribute_value = match.group(4)
        if not match:
            print("** class name missing **")
        elif class_name not in storage.classes():
            print("** class doesn't exist **")
        elif instance_id is None:
            print("** instance id missing **")
        else:
            key = f"{class_name}.{instance_id}"
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute_name:
                print("** attribute name missing **")
            elif not attribute_value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', attribute_value):
                    if '.' in attribute_value:
                        cast = float
                    else:
                        cast = int
                else:
                    attribute_value = attribute_value.replace('"', '')
                instances = storage.attributes()[class_name]
                if attribute_name in instances:
                    attribute_value = instances[attribute_name](attribute_value)
                elif cast:
                    try:
                        attribute_value = cast(attribute_value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute_name, attribute_value)
                storage.all()[key].save()




if __name__ == '__main__':
    HBNBCommand().cmdloop()
