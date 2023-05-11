import cmd
'''File to import'''

class HBNBCommand(cmd.Cmd):
    '''Class blah blah blah'''

    prompt = "(hbnb) "
    def do_EOF(self, arg):
        return True

    def do_quit(self, arg):
        return True

    def emptyline(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
