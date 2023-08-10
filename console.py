#!/usr/bin/python3
"""The module contains the HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        The class contains the entry point of the command
        intepreter with the custom prompt (hbnb)
    """
    prompt = "(hbnb) "

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
