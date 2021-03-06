# -*- coding: utf-8 -*-

"""
    Musichaos CLI
"""

import sys
import click

from .core import Musichaos
from .errors import MusichaosError


@click.command()
@click.argument("rootdir", nargs=1, type=click.Path(exists=True))
@click.argument("targetdir", default=None, type=click.Path(exists=True))
@click.option("-l", "--link", is_flag=True, help="Link audio files isntead of move.")
@click.option("--dry-run", is_flag=True, help="Run a dry run.")
def main(rootdir, targetdir, link, dry_run):
    """
        Tidy up your music chaos.
    """
    musichaos = Musichaos(rootdir)
    try:
        musichaos.tidy_up(targetdir, link, dry_run)
    except MusichaosError as e:
        sys.stderr.write("Error: '{0}'\n".format(e))
        return 1
    else:
        print("Tidy up inside {0} was successful".format(musichaos.rootdir))
        return 0

if __name__ == "__main__":
    sys.exit(main())  # pylint: disable=no-value-for-parameter
