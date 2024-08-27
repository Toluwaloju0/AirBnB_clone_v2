#!/usr/bin/python3
"""A module to deploy a web static content"""

from fabric.api import *

archive = __import__('1-pack_web_static').do_pack()
do_deploy = __import__('2-do_deploy_web_static').do_deploy
# env.hosts = ['54.152.6.186', '35.153.51.170']


def deploy():
    """The function to deploy the code"""

    if archive is None:
        return False
    return do_deploy(archive)
