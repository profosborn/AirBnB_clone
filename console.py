#!/usr/bin/python3
"""The module contains the HBNBCommand class"""
import cmd
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """
        The class contains the entry point of the command
        intepreter with the custom prompt (hbnb)
    """
    prompt = "(hbnb) "
    valid_classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
    ]

    def do_create(self, line):
        if line:
            match line:
                case "BaseModel":
                    new_model = BaseModel()
                    new_model.save()
                    print(new_model.id)
                case "User":
                    new_model = User()
                    new_model.save()
                    print(new_model.id)
                case "State":
                    new_model = State()
                    new_model.save()
                    print(new_model.id)
                case "City":
                    new_model = City()
                    new_model.save()
                    print(new_model.id)
                case "Amenity":
                    new_model = Amenity()
                    new_model.save()
                    print(new_model.id)
                case "Place":
                    new_model = Place()
                    new_model.save()
                    print(new_model.id)
                case _:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        if line:
            args = line.split()
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                allobjects = storage.all()
                key = args[0] + "." + args[1]
                found = allobjects.get(key, None)
                if found:
                    print(found)
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        if line:
            args = line.split()
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                allobjects = storage.all()
                key = args[0] + "." + args[1]
                found = allobjects.get(key, None)
                if found:
                    deleted = allobjects.pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        allobjects = storage.all()
        if line:
            args = line.split()
            if args[0] in HBNBCommand.valid_classes:
                classlist = [str(val) for key, val in allobjects.items()
                        if key.startswith(args[0])]
                print(classlist)
            else:
                print("** class doesn't exist **")
        else:
            allclass = [str(val) for val in allobjects.values()]
            print(allclass)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating
        attribute (save the changes into the JSON file)
        """
        if line:
            args = line.split()
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                allobjects = storage.all()
                key = args[0] + "." + args[1]
                found = allobjects.get(key, None)
                if found:
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        setattr(found, args[2], ast.literal_eval(args[3].strip()))
                        found.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """quits the command interpreter"""
        print
        return True

    def emptyline(self):
        """does nothing when there's no command"""
        return False

if __name__=='__main__':
    HBNBCommand().cmdloop()
