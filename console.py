#!/usr/bin/python3
"""
 This module contains the entry point of the command interpreter
"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review

class_list = ["User", "BaseModel", "Place", "State", "City",
              "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def print_error(self, *to_verify):
        """ Verify errors in line parameter """
        """ Returns False and prints error in case of error """
        """ or returns True in case of non error """
        arguments = to_verify[0].split(' ', 1)

        if len(to_verify[0]) == 0:
            print("** class name missing **")
            return False
        elif arguments[0] not in class_list:
            print("** class doesn't exist **")
            return False
        elif len(to_verify) > 1:
            if len(arguments) < 2:
                print("** instance id missing **")
                return False
        else:
            return True

    def do_EOF(self, line):
        """Quit command to exit the program \n"""
        print()
        sys.exit(0)

    def do_quit(self, line):
        """Quit command to exit the program \n"""
        sys.exit(0)

    def do_create(self, line):
        """ Create and save a new instance """
        class_dict = {"User": User, "BaseModel": BaseModel,
                      "Place": Place, "State": State,
                      "City": City, "Amenity": Amenity,
                      "Review": Review}
        arguments = line.split(' ', 1)
        verify_error = self.print_error(line)
        if verify_error is True:
            class_name = arguments[0]
            new_obj = class_dict[class_name]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance """
        verify_error = self.print_error(line, "verify id")
        if verify_error is not False:
            arguments = line.split(' ', 1)
            key_name = arguments[0] + "." + arguments[1]
            obj = storage.find_key(key_name)
            if obj is not None:
                print(obj)

    def do_destroy(self, line):
        """ Deletes an instance """
        verify_error = self.print_error(line, "verify id")
        if verify_error is not False:
            arguments = line.split(' ', 1)
            key_name = arguments[0] + "." + arguments[1]
            obj = storage.find_key(key_name)
            if obj is not None:
                storage.all().pop(key_name)
                storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances """
        arguments = line.split(' ', 1)
        all_objs = storage.all()
        inst_list = []
        if len(all_objs) > 0:
            if len(line) == 0:
                for key, value in all_objs.items():
                    inst_list.append(str(value))
                print(inst_list)
            elif arguments[0] in class_list:
                for key, value in all_objs.items():
                    answer = key.find(arguments[0], 0, len(arguments[0]))
                    if answer != -1:
                        inst_list.append(str(value))
                print(inst_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance by adding or updating attribute """
        verify_error = self.print_error(line, "verify id")
        if verify_error is not False:
            arguments = line.split(' ', 4)
            key_name = arguments[0] + "." + arguments[1]
            obj = storage.find_key(key_name)
            if obj is None:
                return
            if len(arguments) < 3:
                print("** attribute name missing **")
                return
            elif len(arguments) < 4:
                print("** value missing **")
                return
            obj.save()
            obj.update_instance(arguments[2], arguments[3])
            storage.update_file(obj, key_name)

    def do_count(self, arg):
        count = 0
        for key in storage.all():
            if arg in key:
                count += 1
        print(count)

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
