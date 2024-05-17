#!/usr/bin/env python3

import cmd
import sys
import models
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class."""

    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            class_ = getattr(models, arg)  # Get class from models module
            obj = class_()
            obj.save()
            print(obj.id)
        except AttributeError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            objs = storage.get(cls_name, obj_id)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)
        except  Exception as e:
            print(f"** {e} **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            objs = models.storage.all()
            key = "{}.{}".format(cls_name, obj_id)
            if key in objs:
                objs.pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name.
        """
        objs = models.storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            try:
                cls_name = arg.split()[0]
                print([str(obj) for key, obj in objs.items() if cls_name in key])
            except Exception as e:
                              print(f"** {e} **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
            objs = models.storage.all()
            key = "{}.{}".format(cls_name, obj_id)
            if key in objs:
                obj = objs[key]
                setattr(obj, attr_name, attr_value)
                models.storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the console."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
