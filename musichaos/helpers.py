# -*- coding: utf-8 -*-

"""
    This module contains some helper
    functions for the core module.
"""

import os


def create_directory(path, dry_run=False):
    """
        Creates the given directory path.

        :param str path: the path to the new directory
        :param bool dry_run: flag if it's only a dry run
    """
    if dry_run:
        print("Creating directory:", path)
    else:
        os.mkdir(path)


def move_file(src, dest, dry_run=False):
    """
        Moves the given source path to the
        given destination path.

        :param str src: the path to the source file
        :param str dest: the path to the destination file
        :param bool dry_run: flag if it's only a dry run
    """
    if dry_run:
        print("Moving file from '{0}' to '{1}'".format(
            src, dest))
    else:
        os.rename(src, dest)


def link_file(src, dest, dry_run=False):
    """
        Links the given source path to the
        given destination path.

        :param str src: the path to the source file
        :param str dest: the path to the destination file
        :param bool dry_run: flag if it's only a dry run
    """
    if dry_run:
        print("Linking file from '{0}' to '{1}'".format(
            src, dest))
    else:
        os.symlink(src, dest)


def fix_for_path(string):
    """
        Fixes special path characters in a
        given string to make it usuable in
        a file or directory name.

        :param str string: the string to fix

        :returns: the fixed string
        :rtype: str
    """
    return string.replace("/", "_")
