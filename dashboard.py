"""


§  [ LICENSE ]  ( Apache License Version 2.0 )  :

Copyright [ 2025 ] [ Gustavo Madureira ]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


§  [ ABOUT ]  :

Automated program for creating panels, in order to present the
performance of PMOC and other Services, from the company T.R. MARAZZATTO
to industries such as Unilever and others.

*** FOR INTERNAL PURPOSES ONLY ***

Works on Python 3.12 or higher.


    Source code:

            https://github.com/gtmadureira/trm-dashboard/blob/main/dashboard.py


    Author information:

            Name:
            • Gustavo Madureira (gtmadureira@gmail.com)

            Webpage:
            • https://gtmadureira.github.io/


"""


from multiprocessing import Process, Queue, cpu_count
from multiprocessing.pool import ThreadPool
from os import name as system_type
from os import system as run_command
from sys import exit as close_program
from time import sleep
from types import NoneType
from typing import Any, Final, Tuple, Union

# from audioplayer import AudioPlayer, abstractaudioplayer
from colorama import just_fix_windows_console
from requests import get as get_from_api
from requests.exceptions import (ContentDecodingError, FileModeWarning,
                                 JSONDecodeError, RequestException,
                                 RequestsWarning, StreamConsumedError)


def data_export(queue: Queue) -> None:
    """
    Explanation of the "data_export" function:
    """
    while True:
        data = ("Program under development!")
        queue.put(data, block=False)
        assert isinstance(queue, object)


'''
def play_alert() -> None:
    """
    Plays this alert sound if any Bitcoin address with a positive
    balance is found.
    """
    try:
        player = AudioPlayer("alert.mp3")
        player.volume = 100
        playback_counter = 3
        while playback_counter > 0:
            player.play(loop=False, block=True)
            player.stop()
            playback_counter -= 1
        player.close()
    except (FileNotFoundError, abstractaudioplayer.AudioPlayerError):
        pass
'''


def worker(queue: Queue) -> None:
    """
    Explanation of the "worker" function:
    """
    assert isinstance(queue, object)
    while True:
        if not queue.empty():
            data = queue.get(block=True)
            print(data)


def thread() -> Any:
    """
    CPU thread process for "data_export()" and "worker()" functions.
    """
    processes = []
    data: object = Queue()
    data_factory = Process(target=data_export, args=(data,))
    data_factory.daemon = True
    processes.append(data_factory)
    data_factory.start()
    work = Process(target=worker, args=(data,))
    work.daemon = True
    processes.append(work)
    work.start()
    data_factory.join()


if __name__ == "__main__":

    # This code is a part of a larger program that creates a dashboard for
    # monitoring the performance of PMOC and other Services. It uses the
    # `multiprocessing` library to create a pool of threads that can run
    # concurrently. The `ThreadPool` is created with a number of processes
    # equal to twice the number of CPU cores available on the machine. The
    # `pool.map` function is used to apply the `thread()` function to a range
    # of values, which in this case is just a single value (0 to 1). This
    # allows the program to run in a single-threaded mode, which is useful for
    # debugging or testing purposes. If an exception occurs during the
    # execution of the `pool.map` function, the program will catch the
    # exception and close the pool of threads.
    # The `close_program` function is called to display an error message and
    # terminate the program if an error occurs.
    # The `if __name__ == "__main__":` block ensures that this code is only
    # executed when the script is run directly, and not when it is imported as
    # a module in another script.

    if "example":
        try:
            pool = ThreadPool(processes=cpu_count() * 2)
            # Set to a single CPU thread.
            pool.map(lambda _: thread(), range(0, 1))
        except Exception:
            pool.close()
            close_program("""\033[91m\33[1;7m
[-----------------------------------------------------------------------------]
[                                                                             ]
[     *** Something bad happened and the program had to be shut down ***      ]
[                                                                             ]
[  Possible error :                                                           ]
[                                                                             ]
[ [X] Problem in task processing/multi-processing !                           ]
[                                                                             ]
[-----------------------------------------------------------------------------]
\033[0m""")
        finally:
            pool.close()
            pool.join()
    else:
        pass
