#!/usr/bin/env python3
"""
Simple command interpreter for alu-AirBnB_clone.

Supports:
  create <ClassName>
  show <ClassName> <id>
  destroy <ClassName> <id>
  all [<ClassName>]
  update <ClassName> <id> <attr_name> "<attr_value>"
  quit / EOF
"""
import cmd
import shlex
from models import storage  # storage singleton
from models.base_model import BaseModel


CLASSES = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the project."""

    prompt = "(airbnb) "

    def emptyline(self):
        """Do nothing on empty input instead of repeating last command."""
        pass

    def do_quit(self, arg):
        """Quit the console."""
        return True

    def do_EOF(self, arg):
        """Handle EOF to exit."""
        print()
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel and print its id."""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in CLASSES:
            print("** class doesn't exist **")
            return
        instance = CLASSES[cls_name]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show string representation of an instance by class and id."""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name, obj_id = args[0], args[1]
        key = "{}.{}".format(cls_name, obj_id)
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        print(obj)

    def do_all(self, line):
        """Print all string representations optionally filtered by class."""
        args = shlex.split(line)
        objs = storage.all()
        out = []
        if args:
            cls_name = args[0]
            if cls_name not in CLASSES:
                print("** class doesn't exist **")
                return
            for k, v in objs.items():
                if k.startswith(cls_name + "."):
                    out.append(str(v))
        else:
            out = [str(v) for v in objs.values()]
        print(out)

    def do_destroy(self, line):
        """Destroy an instance by class name and id."""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, line):
        """Update an instance's attribute: update Class id attr value."""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        attr_name = args[2]
        attr_value = args[3]
        # basic type inference: try int, float else string
        try:
            if attr_value.isdigit():
                val = int(attr_value)
            else:
                val = float(attr_value)
        except Exception:
            val = attr_value.strip('"').strip("'")
        setattr(obj, attr_name, val)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
