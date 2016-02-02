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
@click.option("-l", "--link", is_flag=True)
@click.option("--dry-run", is_flag=True)
def main(rootdir, targetdir, link, dry_run):
    """
        Tidy up your music chaos.
    """
    musichaos = Musichaos(rootdir)
    try:
        musichaos.tidy_up(targetdir, link, dry_run)
    except MusichaosError as e:
        print("Error: '{0}'".format(e), file=sys.stderr)
        return 1
    else:
        print("Tidy up inside {0} was successful".format(musichaos.rootdir))
        return 0

if __name__ == "__main__":
    sys.exit(main())  # pylint: disable=no-value-for-parameter
