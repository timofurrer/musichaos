# -*- coding: utf-8 -*-

"""
    This module is a collection of all possible
    musichaos errors.
"""


class MusichaosError(Exception):
    """Base exception for all Musichaos specific errors."""
    pass


class UnrecognizedFormat(MusichaosError):
    """
        Exception which is raised if a found audio file
        is not supported.
    """
    def __init__(self, fileformat):
        super(UnrecognizedFormat, self).__init__(
            "Format '{0}' is unrecognized".format(fileformat))
