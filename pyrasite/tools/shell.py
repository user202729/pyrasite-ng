# This file is part of pyrasite.
#
# pyrasite is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyrasite is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyrasite.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2011-2013 Red Hat, Inc., Luke Macken <lmacken@redhat.com>

import os
import sys
import pyrasite


def shell():
    """Open a Python shell in a running process"""

    import argparse
    from pyrasite.main import add_common_arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("pid", type=int,
                        help="The ID of the process to inject code into")
    add_common_arguments(parser)
    args = parser.parse_args()
    pid = args.pid

    ipc = pyrasite.PyrasiteIPC(pid, 'ReversePythonShell',
                               timeout=os.getenv('PYRASITE_IPC_TIMEOUT') or args.ipc_timeout,
                               verbose=args.verbose, gdb_prefix=args.gdb_prefix)
    ipc.connect()

    print("Pyrasite Shell %s" % pyrasite.__version__)
    print("Connected to '%s'" % ipc.title)

    prompt, payload = ipc.recv().split('\n', 1)
    print(payload)

    try:
        import readline
    except ImportError:
        pass

    # py3k compat
    try:
        input_ = raw_input
    except NameError:
        input_ = input

    try:
        while True:
            try:
                input_line = input_(prompt)
            except EOFError:
                input_line = 'exit()'
                print('')
            except KeyboardInterrupt:
                input_line = 'None'
                print('')

            ipc.send(input_line)
            payload = ipc.recv()
            if payload is None:
                break
            prompt, payload = payload.split('\n', 1)
            if payload != '':
                print(payload)
    except:
        print('')
        raise
    finally:
        ipc.close()


if __name__ == '__main__':
    shell()
