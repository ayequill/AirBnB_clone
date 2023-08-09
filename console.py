#!/usr/bin/python3
""" This module contains HBNB CLI Interpreter """
from cmd import Cmd
from models.base_model import BaseModel as Base
import models

classes = {
    'BaseModel': 'BaseModel'
}


class HBNBCommand(Cmd):
    """
    Class representing the hbnb CLI.
    """
    prompt = "(hbnb) "
    __storage = models.storage

    # Instance Commands

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
        elif line != "BaseModel":
            print("** class doesn't exist **")
            return
        else:
            new_instance = Base()
            new_instance.save()
            print(new_instance.id)
    # TODO Refactor conditions

    def do_show(self, line):
        """ Prints a specific object provided the
            ID and class name """
        args = line.partition(" ")
        instance_name = args[0]
        instance_id = args[2]

        if not instance_name:
            print("** class name missing **")
            return
        if instance_name not in classes:
            print("** class doesn't exist **")
            return
        if instance_name in classes and not instance_id:
            print("** instance id missing **")

        try:

            key = instance_name + "." + instance_id
            print(HBNBCommand.__storage.all()[key])
        except KeyError:
            if instance_name in classes and instance_id:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.partition(" ")
        instance_name = args[0]
        instance_id = args[2]

        if not instance_name:
            print("** class name missing **")
            return
        if instance_name not in classes:
            print("** class doesn't exist **")
            return
        if not instance_id:
            print("** instance id missing **")

        try:
            key = instance_name + "." + instance_id
            del HBNBCommand.__storage.all()[key]
            HBNBCommand.__storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances
            based or not on the class name """
        list_to_print = []

        if args:
            instance_name = args.split(" ")[0]
            if instance_name not in classes:
                print("** class doesn't exist **")
                return

            for key, value in HBNBCommand.__storage.all().items():
                if key.split(".")[0] == instance_name:
                    list_to_print.append(str(value))
        else:
            list_to_print = [str(obj)
                             for obj in HBNBCommand.__storage.all().values()]
        print(list_to_print)

    def do_update(self, arg):
        """ Updates an instance based on the class name
            and id by adding or updating attribute """

        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]

        if cls_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_objs = HBNBCommand.__storage.all()
        key = cls_name + "." + instance_id

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        instance = all_objs[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    # Main Commands

    def do_quit(self, line):
        """ Exits the console """
        return True

    def do_EOF(self, line):
        """ End of line marker """
        print()
        return True

    def emptyline(self):
        """ Ignore empty lines """
        pass

    # Help Documentation

    def help_quit(self):
        """ Quit Command Help """
        print("Quit command to exit the program\n")

    def help_create(self):
        """ Help for create command """
        print("Creates a class")
        print("[Usage]: create <classname>\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
