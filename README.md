# Roku Remote

Roku command line interface and python REPL

## Install

```shell
cd path/to/roku-remote
pip install .
```

## Command Line Interface

from `roku --help`

```comment
usage: roku [-h] [--app APP] [--discover] --host HOST [--list-apps]
            [--list-commands] [--interact] [--timeout-s TIMEOUT_S]
            [command]

Roku command line interface and python REPL

positional arguments:
  command               command to run

options:
  -h, --help            show this help message and exit
  --app APP             launch an app by name (case-insensitive)
  --discover            Use SSDP to find rokus on local networks
  --host HOST           host name or IP address
  --list-apps           print installed apps and exit
  --list-commands       print supported commands and exit
  --interact            enter interactive python REPL
  --timeout-s TIMEOUT_S
                        set the TCP/HTTP timeout time, in seconds
```

### Apps

The `--app` argument launches an app by name. The app argument is *case-insensitive*.

Argument `--list-apps` prints a list of names of the installed apps. These names can be used with the argument `--app`.

### Commands

The `--command` argument executes a command. The command argument is *case-sensitive*.

Argument `--list-commands` prints a list of supported commands. These commands can be used with the argument `--command`.

## References

This package is simply a wrapper for python package `roku`. For more information, see:

[https://github.com/jcarbaugh/python-roku](https://github.com/jcarbaugh/python-roku)
