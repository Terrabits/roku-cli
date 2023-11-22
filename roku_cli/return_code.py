from enum import IntEnum


class ReturnCode(IntEnum):

    SUCCESS = 0

    # errors  

    ERROR_TOO_MANY_EXE_ARGS    = 1
    ERROR_COMMAND_MISSING      = 2
    ERROR_APP_NOT_FOUND        = 3
    ERROR_COMMAND_NOT_FOUND    = 4
    ERROR_CONNECTION_TIMED_OUT = 5
