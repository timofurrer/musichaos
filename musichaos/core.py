# -*- coding: utf-8 -*-

"""
    Musichaos is able to bring tidiness into
    your music collection which is probably
    organized in a absolute chaos.
"""

import os
import glob
import itertools
import mutagen

from .helpers import create_directory, move_file, link_file
from .helpers import fix_for_path
from .errors import UnrecognizedFormat


class Musichaos(object):
    """
        Brings tidiness into your chaos of music
        files you've downloaded from somewhere.

        Musichaos supports all audio file formats supported
        by mutagen. These are currently the following formats:
            * ASF (*.asf)
            * FLAC (*.flac)
            * M4A (*.m4a)
            * Monkey's Audio (*.ape)
            * MP3 (*.mp3)
            * Musepack (*.mpc, *.mp+, *.mpp)
            * Ogg Opus, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis
                (*.ogg, *.ogv, *.oga, *.ogx, *.ogm, *.spx, *opus)
            * True Audio (*.tta)
            * WavPack (*.wv)
            * OptimFROG (*.mp3)
            * AIFF (*.aiff, *.aif, *.aifc)
    """
    SUPPORTED_FORMATS = [
        "*.asf", "*.flac", "*.m4a", "*.ape", "*.mp3", "*.mpc", "*.mp+", "*.mpp",
        "*.ogg", "*.ogv", "*.oga", "*.ogx", "*.ogm", "*.spx", "*.ogus", "*.tta",
        "*.wv", "*.aiff", "*.aif", "*aifc"
    ]

    def __init__(self, rootdir):
        self.rootdir = rootdir

    def tidy_up(self, targetdir=None, linking=False, dry_run=False):
        """
            Tidy ups the music chaos inside
            the ``rootpath``. The music files are
            ordered by Interpreters, Albums and other
            information found in the tags of the audio files.

            :param str targetpath: the root dir of where to
                                   store the the clean music structure
            :param bool linking: flag if files should be linked
                                 instead of moved
            :param bool dry_run: flag if it's only a dry run
        """
        if targetdir is None:
            targetdir = self.rootdir

        for audiofile_path in self.get_audio_files():
            audio_file = mutagen.File(audiofile_path, easy=True)
            audio_fileext = os.path.splitext(audiofile_path)[-1]
            if not audio_file:
                raise UnrecognizedFormat(audio_fileext)

            artist = self.get_audio_tag(audio_file, "artist")
            album = self.get_audio_tag(audio_file, "album")
            title = self.get_audio_tag(audio_file, "title")

            artist_dir = os.path.join(targetdir, fix_for_path(artist))
            album_dir = os.path.join(artist_dir, fix_for_path(album))
            title_filename = "{0}{1}".format(fix_for_path(title), audio_fileext)
            title_file = os.path.join(album_dir, title_filename)

            if not os.path.exists(artist_dir):
                create_directory(artist_dir, dry_run)

            if not os.path.exists(album_dir):
                create_directory(album_dir, dry_run)

            if os.path.exists(title_file):  # audio file already exists
                continue

            if linking:
                rellink_src = os.path.relpath(audiofile_path, album_dir)
                link_file(rellink_src, title_file, dry_run)
            else:
                move_file(audiofile_path, title_file, dry_run)

    def get_audio_files(self):
        """
            Gets all audio files underneath the
            root directory.

            :returns: list of audio file paths
            :rtype: list
        """
        print(glob.iglob)
        return itertools.chain.from_iterable(
            glob.iglob(os.path.join(self.rootdir, pattern))
            for pattern in self.SUPPORTED_FORMATS)

    @staticmethod
    def get_audio_tag(audiofile, name):
        """
            Gets a specific tag from a given audio file.

            :param mutagen.File audiofile: the audio file to get the tags from
            :param str name: the tag name to find

            :returns: the tags value
            :rtype: str
        """
        values = audiofile.get(name)
        if not values:
            return None

        return values[0]
