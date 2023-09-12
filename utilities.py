import os
import errno
import shutil
import uuid
from datetime import datetime


def genUniqueId():
    return str(uuid.uuid4())


def getTimestamp():
    return datetime.now().strftime('%Y-%m-%dT%H-%M-%S')


def backupDb(dbname, backupdir):
    filename = "{}_{}.db".format(
        dbname.replace(".db", ""),
        getTimestamp()
    )
    try:
        os.mkdir(backupdir)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    try:
        shutil.copyfile(dbname, "{}{}".format(backupdir, filename))
    except FileNotFoundError:
        print("Creating db")
