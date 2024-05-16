import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is reached"""
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
