

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
                command = ["mysqldump", f"-u{username}", f"-p{password}", db_name]
                with open(backup_file, "w") as file:
                    subprocess.run(command, stdout=file, check=True)
            case "postgresql":
                command = ["pg_dump", "-U", username, "-F", "c", "-b", "-v", "-f", backup_file, db_name]
                subprocess.run(command, check=True)
            case "mongodb":
                command = ["mongodump", "--db", db_name, "--out", backup_file]
                subprocess.run(command, check=True)
            case "sqlite":
                shutil.copyfile(db_name, backup_file)
    except subprocess.CalledProcessError:
        print("Error occurred during backup")
    return backup_file

                