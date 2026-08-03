

print(r"""

 ██████████   ███████████                                   ████   █████   
░░███░░░░███ ░░███░░░░░███                                 ░░███  ░░███    
 ░███   ░░███ ░███    ░███ █████ █████  ██████   █████ ████ ░███  ███████  
 ░███    ░███ ░██████████ ░░███ ░░███  ░░░░░███ ░░███ ░███  ░███ ░░░███░   
 ░███    ░███ ░███░░░░░███ ░███  ░███   ███████  ░███ ░███  ░███   ░███    
 ░███    ███  ░███    ░███ ░░███ ███   ███░░███  ░███ ░███  ░███   ░███ ███
 ██████████   ███████████   ░░█████   ░░████████ ░░████████ █████  ░░█████ 
░░░░░░░░░░   ░░░░░░░░░░░     ░░░░░     ░░░░░░░░   ░░░░░░░░ ░░░░░    ░░░░░  

""")
import subprocess

def backup(username, password, db_type, db_name, backup_file):
    try:
        if db_type == "mysql":
            command = ["mysqldump", f"-u {username}", f"-p{password}", db_name] # used a list to avoid using shell=True
            with open(backup_file) as f:
                subprocess.STDOUT = f
                subprocess.run(command, check=True) # check = true so that first except can get triggered
                