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
        'User': User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)


    def do_show(self, arg):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name.
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif arg in self.classes:
            print([str(obj) for obj in storage.all().values() if type(obj).__name__ == arg])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
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


    def default(self, arg):
        """Override the default method to handle <class name>.all() and <class name>.count()"""
        args = arg.split('.')
        if len(args) == 2:
            class_name = args[0]
            command = args[1]
            if class_name in self.classes:
                if command == "all()":
                    instances = [str(obj) for obj in storage.all().values() if type(obj).__name__ == class_name]
                    print(instances)
                elif command == "count()":
                    count = len([obj for obj in storage.all().values() if type(obj).__name__ == class_name])
                    print(count)
                else:
                    print("*** Unknown syntax: {}".format(arg))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(arg))

if __name__ == '__main__':
    HBNBCommand().cmdloop()

