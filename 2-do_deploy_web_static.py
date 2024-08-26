#!/usr/bin/python3
"""A script to deploy the web_static files"""

from fabric.api import run, env, local, put

env.hosts = ['54.152.6.186', '35.153.51.170']


def do_deploy(archive_path):
    """The function to deploy the code to the server
    Args:
       archive_path: the path to the file
    """
    env.hosts = ['54.152.6.186', '35.153.51.170']
    try:
        with open(archive_path, 'r') as a:

    except FileNotFoundError:
        return False

    put(archive_path, f"/tmp/{archive_path}")
    main_archive = archive_path.split('/')[1]
    new_path = main_archive[:-4]
    run(f"mkdir -p /data/web_static/releases/{new_path}")
    folder = f"/data/web_static/releases/{new_path}"
    # unpack the archive
    unpack = run(f"tar -xzf /tmp/{main_archive} -C {folder}")
    run(f"rm /tmp/{main_archive}")
    run("rm -rf /data/web_static/current")
    run(f"ln -s /data/web_static/releases/{new_path} /data/web_static/current")
    print("New version deployed!")
    return True