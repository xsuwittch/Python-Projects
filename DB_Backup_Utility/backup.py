

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
import shutil


def backup(username, password, db_type, db_name, backup_file):
    try:
        match db_type:
            case "mysql":
                command = ["mysqldump", f"-u{username}", f"-p{password}", db_name] # used a list to avoid using shell=True
            case "postgresql":
                command = ["pg_dump", "-U", username, "-F", "c", "-b", "-v", "-f", backup_file, db_name]
            case "mongodb":
                command = ["mongodump", "--db", db_name, "--out", backup_file]
            case "sqlite":
                shutil(db_name,backup_file)
        with open (backup_file, w) as file:
            subprocess.STDOUT = file
            subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(" Error Occured during backup")
    return backup_file


                