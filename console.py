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
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """
        The class contains the entry point of the command
        intepreter with the custom prompt (hbnb)
    """

    prompt = '(hbnb) '

    valid_classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]

    def do_create(self, line):
        """Usage: create <classname>"""
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
                case "Review":
                    new_model = Review()
                    new_model.save()
                    print(new_model.id)
                case _:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Usage: show <classname> <instance-id>"""
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
        """Usage: destroy <classname> <instance-id>"""
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
        """Usage: all or all <classname>"""
        allobjs = storage.all()
        if line:
            args = line.split()
            if args[0] in HBNBCommand.valid_classes:
                classlist = [
                    str(val) for key, val in allobjs.items()
                    if key.startswith(args[0])
                ]
                print(classlist)
            else:
                print("** class doesn't exist **")
        else:
            allclass = [str(val) for val in allobjs.values()]
            print(allclass)

    def do_update(self, line):
        """ Usage: update <classname> <id> <attribute-name> <"value">"""
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
                        try:
                            setattr(
                                found,
                                args[2],
                                ast.literal_eval(args[3].strip())
                            )
                        except (ValueError):
                            setattr(found, args[2], args[3])
                        found.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def _do_update_dict(self, line, classname):
        """Usage: <class name>.update(<id>, <dictionary>)"""
        args = line.split(',', 1)
        try:
            new_dict = ast.literal_eval(args[1].strip())
            if type(new_dict) is not dict:
                print("** Invalid dictionary **")
                return
            key_id = "{}.{}".format(classname, args[0].strip('"').strip())
            obj = storage.all().get(key_id, None)

            if obj is None:
                print("** no instance found **")
                return

            for key in new_dict:
                setattr(obj, key, new_dict[key])
        except BaseException:
            print("** Invalid dictionary **")

    def _do_count(self, line):
        """Usage: <classname>.count()"""
        model_name = line.split()[0]
        keys = [key for key in storage.all().keys()
                if key.startswith(model_name)]
        print(len(keys))

    def default(self, line):
        """Executes all other commands"""
        methods = {
            'count': self._do_count,
            'all': self.do_all,
            'show': self.do_show,
            'update': self.do_update,
            'destroy': self.do_destroy
        }
        commands = line.split('.', 1)

        if len(commands) == 1:
            print(f'*** Unknown syntax: {line}')
            return

        do_method = commands[1].split("(", 1)

        if do_method[0] not in methods or len(do_method) < 2:
            print(f'*** Unknown syntax: {line}')
            return

        if (len(commands[0].strip()) < 1):
            print("** class name missing **")
            return

        if (commands[0] not in HBNBCommand.valid_classes):
            print("** class doesn't exist **")
            return

        do_method[1] = do_method[1].strip()
        if len(do_method[1]) < 1 or do_method[1][-1] != ')':
            print(f'*** Unknown syntax: {line}')
            return
        args = do_method[1][:-1]

        if do_method[0] == 'update':
            if (len(args) < 1):
                print("** no instance found **")
                return

            new_attrs = args.split(',', 1)

            if len(new_attrs) < 2:
                print("** attribute name missing **")
                return

            if new_attrs[1].strip()[0] == '{':
                self._do_update_dict(args, commands[0])
            else:
                args = args.strip().replace(',', '')
                new_line = "{} {}".format(commands[0], args)
                new_line = new_line.replace('"', '')
                print(new_line)
                return self.do_update(new_line)
        else:
            new_line = '{} {}'.format(commands[0], args)
            return methods[do_method[0]](new_line)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """quits the command interpreter"""
        print("")
        return True

    def emptyline(self):
        """does nothing when there's no command"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
