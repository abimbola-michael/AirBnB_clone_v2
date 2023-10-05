#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""

from os.path import exists
from fabric.api import put, env, run
env.hosts = ['52.3.220.197', '54.82.207.84']


def do_deploy(archive_path):
    """script that distributes an archive to web servers"""
    if not exists(archive_path):
        return False
    try:
        a_file = archive_path.split("/")[-1]
        f_name = a_file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('rm -rf {}{}/'.format(path, f_name))
        run('mkdir -p {}{}/'.format(path, f_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(a_file, path, f_name))
        run('rm /tmp/{}'.format(a_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, f_name))
        run('rm -rf {}{}/web_static'.format(path, f_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, f_name))
        return True
    except Exception:
        return False
