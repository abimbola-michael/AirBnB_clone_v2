#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""

from os.path import exists
from fabric.api import put, env, run
env.hosts = ['52.3.220.197', '54.82.207.84']


def do_deploy(archive_path):
    """scripty that distributes an archive to web servers"""
    if exists(archive_path) is False:
        return False
    try:
        a_file = archive_path.split("/")[-1]
        ext = a_file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(a_file, path, ext))
        run('rm /tmp/{}'.format(a_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext))
        run('rm -rf {}{}/web_static'.format(path, ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ext))
        return True
    except:
        return False
