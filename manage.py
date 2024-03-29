#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from college_setup import college_setup


def main():
    args = sys.argv
    if args[1] == "runserver" and not os.environ.get("RUN_MAIN", False):
        """Execute this code everytime the server start"""
        status = college_setup()
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_voting.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
