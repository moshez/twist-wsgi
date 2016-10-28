#!/usr/bin/env python
import os
import subprocess
import sys

env = os.environ.copy()
env['PYTHONPATH'] = os.getcwd()
WSGI = 'bo_sayhello.app'
subprocess.check_call(["twist", "web", "--wsgi", WSGI] + sys.argv[1:],
                      env=env)
