# -*- coding: utf-8 -*-

"""
    Test for the core modules functionality.
"""

from unittest import TestCase
from mock import patch
from random import shuffle

from musichaos import Musichaos


class TestCore(TestCase):
    """
        Test the core module.
    """
    def test_get_audio_files(self):
        """test getting audio files"""

        audio_files = [
            "Song.mp3", "Song.flac", "Song.wv", "Song.mp+"
        ]

        other_files = [
            "Document.docx", "Presentation.pptx", "Document.pdf"
        ]

        musichaos = Musichaos("")

        with patch("glob.iglob") as iglob_patch:
            iglob_patch.return_value = shuffle(audio_files + other_files)

            print("Test", iglob_patch)

            filtered_audio_files = musichaos.get_audio_files()
            print("Audio files", list(filtered_audio_files))

            set(filtered_audio_files).should.be.equal(set(audio_files))
