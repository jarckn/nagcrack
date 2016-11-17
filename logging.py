from enum import Enum
from datetime import datetime


class Color:
    OK = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    INFO = '\033[34m'
    END = '\033[0m'


class Type(Enum):
    OK = 0
    WARNING = 1
    ERROR = 2
    INFO = 3


def writelog(message, types=Type):

    timestamp = datetime.now()
    ts_date = str(timestamp.day) + "\\" + str(timestamp.month) + "\\" + str(timestamp.year)
    ts_time = str(timestamp.hour) + ":" + str(timestamp.minute) + ":" + str(timestamp.second)

    print("[" + ts_date + " " + ts_time + "] [", end='')
    if types == Type.OK:
        print(Color.OK + "OK" + Color.END + "]: ", end='')
    elif types == Type.WARNING:
        print(Color.WARNING + "WARNING" + Color.END + "]: ", end='')
    elif types == Type.ERROR:
        print(Color.ERROR + "ERROR" + Color.END + "]: ", end='')
    elif types == Type.INFO:
        print(Color.INFO + "INFO" + Color.END + "]: ", end='')
    print(message)
