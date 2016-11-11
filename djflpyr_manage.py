#!/usr/bin/env python
import os
import subprocess
import sys

env = os.environ.copy()
env['PYTHONPATH'] = os.getcwd()
subprocess.check_call(["twist", "djflpyr"] + sys.argv[1:],
                      env=env)
