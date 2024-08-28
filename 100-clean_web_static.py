#!/usr/bin/python3
""" A module to clean versions of a file"""

from fabric.api import local, env

env.hosts = ['54.152.6.186', '35.153.51.170']
env.user = 'ubunbtu'

def do_clean(number=0):
    """A code to clean the versions directory"""

    files = local("ls -ltr versions", capture=True)
    files = siles.stdout.split()
    if len(files) < number:
        return None
    # Iterate and delete the files
    for e in range(number, len(files)):
        local(f"rm -f {files[e]")
