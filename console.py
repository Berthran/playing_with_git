#!/usr/bin/python3
import cmd
"""Class instance that inherits from the Cmd class"""


class HBNBCommand(cmd.Cmd):
    """Simple class to build an interpreter
       prompt: custom entry point to the interpreter
    """

    prompt = '(hbnb) '
    def do_EOF(self, arg):
        """Command to handle the EOF"""
        return True
    
    def do_quit(self, arg):
        """Command to exit the program"""
        return True

    def emptyline(self):
        """Command to not execute any empty line entered"""
        pass

    def do_create(self, class_name):
        '''Creates a new class instance and saves it'''
        pass

    def do_show(self, class_name, class_id):
        '''Prints an instance of an object
        represented by class_name and class_id'''
        pass

    def do_destroy(self, class_name, class_id):
        '''Deletes an instance and save changes'''
        pass

    def do_all(self, class_name):
        '''Prints all instances in an object file'''
        pass

    def do_update(self, **kwargs):
        '''Updates a class one attribute per time
        and saves'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
