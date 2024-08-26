#!/usr/bin/python3
"""A module to pac a file content using fabric"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """A function to pack the contents of a directory"""

    date = datetime.now()
    date = str(date)
    date = date.replace('-', "").replace(':', "")\
        .replace(".", "").replace(" ", "")
    date = date[0:-6]
    filename = "web_static_{}.tgz".format(date)
    zip_files = local('mkdir -p versions')
    zip_files = local(f"tar -cvzf versions/{filename} web_static")
    if zip_files.succeeded:
        files = local(f"ls -i versions/{filename}", capture=True)
        files = files.stdout.split()
        print(f"web_static packed: versions/{filename} -> {files[0]}Bytes")
        return (f"versions/{filename}")
