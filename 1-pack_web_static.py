#!/usr/bin/python3
"""
This script generates .tgz archive from the contents of the web_static folder.
"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    
    Returns:
        str: The path of the generated archive if successful, None otherwise.
    """
    dt = datetime.utcnow()
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive_name)).failed is True:
        return None
    return archive_name
