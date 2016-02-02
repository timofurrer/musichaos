# Musichaos
> Bring tidiness into your music chaos

***

`musichaos` is a tool to tidy up the chaos in your local music library on a file basis.
It pulls the tags from the audio files and structures the audio files like this:

```
~/music
│   ├── Artist 01
│   │   └── Album 01
│   │   │   └── Title 01
│   │   │   │── Title 02
│   ├── Artist 02
│   │   └── Album 01
│   │   │   └── Title 01
│   │   │   │── Title 02
```

## Installation

From pip:

```bash
pip install musichaos
```

From source:

```
git clone https://github.com/timofurrer/musichaos
cd musichaos
pip install .
```

## Usage - Command Line Interface

`musichaos` can be used as a CLI tool.

To use it just specify the root directory which contains your music chaos and a target directory where to put the clean structure.
They can point to the same location.

```
musichaos ~/downloads ~/music
```

This will end up in the following structure
```
~/music
│   ├── Artist 01
│   │   └── Album 01
│   │   │   └── Title 01
│   │   │   │── Title 02
│   ├── Artist 02
│   │   └── Album 01
│   │   │   └── Title 01
│   │   │   │── Title 02
```

If you do not want to move the audio file but link them instead - run the following command:
```
musichaos ~/downloads ~/music --link
```

This will end up in the following structure
```
~/music
│   ├── Artist 01
│   │   └── Album 01
│   │   │   └── Title 01 -> ../../../downloads/Some_weird_audio_file_01.mp3
│   │   │   │── Title 02 -> ../../../downloads/Some_weird_audio_file_02.mp3
│   ├── Artist 02
│   │   └── Album 01
│   │   │   └── Title 01 -> ../../../downloads/Some_weird_audio_file_03.mp3
│   │   │   │── Title 02 -> ../../../downloads/Some_weird_audio_file_04.mp3
```

If you are not sure what `musichaos` will do - just do a dry run:

```
musichaos ~/downloads ~/music --dry-run
```

Let's have a look at the help message:

```
Usage: __main__.py [OPTIONS] ROOTDIR TARGETDIR

  Tidy up your music chaos.

Options:
  -l, --link  Link audio files instead of move.
  --dry-run   Run a dry run.
  --help      Show this message and exit.
```

## Usage - Python Package

`musichaos` can be imported in your python project, too. Just install it in your python environment and `import musichaos`:

```python
from musichaos import Musichaos

chaos = Musichaos(rootdir)
chaos.tidy_up(targetdir, link, dry_run)
```

## Supported Audio File Formats

At the moment the following file formats are supported:

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
