#!/usr/bin/python3
"""
a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy
"""

from datetime import datetime
from os.path import exists, isdir
from fabric.api import put, env, local, run
env.hosts = ['52.3.220.197', '54.82.207.84']


def do_pack():
    """script that generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


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
    except:
        return False


def deploy():
    """script that creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
