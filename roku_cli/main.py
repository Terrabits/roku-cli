from   .command_line       import parse
from   .return_code        import ReturnCode
from   code                import interact
from   requests.exceptions import ConnectTimeout, ConnectionError
from   roku                import Roku
from   socket              import gaierror
import sys


# constants
REQUEST_ERRORS = (ConnectTimeout, ConnectionError, gaierror)


def main():

    # parse command line args
    args = parse()


    # --discover?
    if args.discover:
        rokus = Roku.discover(timeout=args.timeout_s)
        for roku in rokus:
            print(roku.host)
        sys.exit(ReturnCode.SUCCESS)


    # handle requests exceptions
    try:

        # create roku object
        roku = Roku(args.host, timeout=args.timeout_s)

        # --list-apps?
        if args.list_apps:
            apps = sorted([app.name[0].upper() + app.name[1:] for app in roku.apps])
            for app in apps:
                print(app)
            sys.exit(ReturnCode.SUCCESS)


        # --list-commands?
        if args.list_commands:
            for command in roku.commands:
                print(command)
            sys.exit(ReturnCode.SUCCESS)


        # --interact?
        if args.interact:
            device_name = roku.device_info.user_device_name
            banner = f"connected to '{device_name}' as roku"
            interact(banner, local={ 'args': args, 'roku': roku })
            sys.exit(ReturnCode.SUCCESS)


        # --app?
        if args.app:

            # get app index
            app_names = [app.name.lower() for app in roku.apps]
            try:
                index = app_names.index(args.app.lower())

            # app index not found?
            except ValueError:
                print(f"error: app '{args.app}' not found")
                print('See --list-apps for a list of installed apps')
                sys.exit(ReturnCode.ERROR_APP_NOT_FOUND)

            # launch app
            app = roku.apps[index]
            roku.launch(app)
            sys.exit(ReturnCode.SUCCESS)


        # execute command

        # get command
        try:
            command = getattr(roku, args.command)

        # command does not exist?
        except AttributeError:
            print(f"error: command '{args.command}' not found")
            print('See --list-commands for a list of supported commands')
            sys.exit(ReturnCode.ERROR_COMMAND_NOT_FOUND)


        # execute command
        command()
        sys.exit(ReturnCode.SUCCESS)


    # connection timed out?
    except REQUEST_ERRORS:
        print(f'error: connection failed')
        sys.exit(ReturnCode.ERROR_CONNECTION_TIMED_OUT)


# execute as main?
if __name__ == '__main__':
    main()
