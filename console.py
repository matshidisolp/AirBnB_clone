#!/usr/bin/env python3

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter class."""

    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
        'User': User
    }

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")


    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        arg_list = args.split()
        if len(arg_list) < 2:
            if not args:
                print("** class name missing **")
            else:
                print("** instance id missing **")
            return
        class_name, instance_id = arg_list
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + instance_id
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        arg_list = args.split()
        if len(arg_list) < 2:
            if not args:
                print("** class name missing **")
            else:
                print("** instance id missing **")
            return
        class_name, instance_id = arg_list
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
        else:
            storage.all().pop(key)
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name.
        """
        if args:
            if args not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
                return
            objects = [str(obj) for key, obj in storage.all().items() if key.startswith(args)]
        else:
            objects = [str(obj) for obj in storage.all().values()]
        print(objects)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute.
        """
        arg_list = args.split()
        if len(arg_list) < 4:
            if not args:
                print("** class name missing **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif len(arg_list) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return
        class_name, instance_id, attr_name, attr_value = arg_list
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + instance_id
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            setattr(obj, attr_name, attr_value)
            obj.save()

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

