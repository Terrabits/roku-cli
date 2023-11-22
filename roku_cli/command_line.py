from   .return_code import ReturnCode
from   argparse     import ArgumentParser
import sys


# create argument parser
parser = ArgumentParser(
    prog='roku',
    description='Roku command line interface and python REPL',
)


# define arguments
parser.add_argument('--app',                                    help='launch an app by name (case-insensitive)')
parser.add_argument('--discover',      action='store_true',     help='Use SSDP to find rokus on local networks')
parser.add_argument('--host',          required=True,           help='host name or IP address')
parser.add_argument('--list-apps',     action='store_true',     help='print installed apps and exit')
parser.add_argument('--list-commands', action='store_true',     help='print supported commands and exit')
parser.add_argument('--interact',      action='store_true',     help='enter interactive python REPL')
parser.add_argument('--timeout-s',     default=3,               help='set the TCP/HTTP timeout time, in seconds')
parser.add_argument('command',         nargs='?', default=None, help='command to run')



def parse():

    # parse
    args = parser.parse_args()


    # validate args

    # get executable argument states -
    #   arguments which perform an action and exit
    exe_arg_states = {
        '--app':           bool(args.app),
        '--discover':      bool(args.discover),
        '--list-apps':     bool(args.list_apps),
        '--list-commands': bool(args.list_commands),
        '--interact':      bool(args.interact),
        'command':         bool(args.command)
    }


    # get list of executable args
    exe_args = list(filter(exe_arg_states.__getitem__, exe_arg_states.keys()))


    # get number of "executable" arguments:
    #   arguments which perform an action and exit
    exe_args_count    = len(exe_args)
    no_exe_args       = exe_args_count == 0
    too_many_exe_args = exe_args_count > 1


    # are there too many executable arguments?
    if len(exe_args) > 1:
        parser.print_usage()
        exe_args_str = ', '.join([f"'{arg}'" for arg in sorted(exe_args)])
        print(f'error: arguments {exe_args_str} cannot be used together')
        sys.exit(ReturnCode.ERROR_TOO_MANY_EXE_ARGS)


    # is positional argument `command` missing?
    if len(exe_args) == 0:
        parser.print_usage()
        print("error: positional argument 'command' is missing")
        sys.exit(ReturnCode.ERROR_COMMAND_MISSING)


    # args are valid (so far)

    return args
