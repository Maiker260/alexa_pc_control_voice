import shutil

def is_installed(cmd):
    return shutil.which(cmd) is not None