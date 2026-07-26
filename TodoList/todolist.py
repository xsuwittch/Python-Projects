print(r"""
___________        .___       .____    .__          __   
\__    ___/___   __| _/____   |    |   |__| _______/  |_ 
  |    | /  _ \ / __ |/  _ \  |    |   |  |/  ___/\   __\
  |    |(  <_> ) /_/ (  <_> ) |    |___|  |\___ \  |  |  
  |____| \____/\____ |\____/  |_______ \__/____  > |__|  
                    \/                \/       \/       
    1: View Tasks
    2: Add Task
    3: Mark as done
    4: Remove Task
    
""")

print("option> ", end="" )
option = int(input())

match option:
    case 1:
        try:
            file = open("tasks.txt","r")
            content = file.read()
            print(content)
            file.close()
        except FileNotFoundError as e:
            print(" Error! Make sure file is in the same folder")
        finally:
            file.close()
    case 2:
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        max_id = 0
        for line in lines:
            if not line.strip():
                continue
            id_, task, status = line.strip().split("|")
            max_id = max(max_id, int(id_.strip()))

        new_id = max_id + 1

        print(" Enter Task: ", end="")
        newtask = input()

        with open("tasks.txt", "a") as file:
            file.write(f"{new_id} | {newtask} | pending\n")

        print(" Task added.")
    case 3:
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(" Error! Make sure file is in the same folder")
            lines = []

        for line in lines:
            if not line.strip():
                continue
            id, task, status = line.strip().split("|")
            print(f"{id.strip()}. {task.strip()} [{status.strip()}]")

        print(" Enter Task ID: ", end="")
        targetid = input().strip()

        found = False
        for i, line in enumerate(lines):
            if not line.strip():
                continue
            id, task, status = line.strip().split("|")
            if id.strip() == targetid:
                lines[i] = f"{id.strip()} | {task.strip()} | done\n"
                found = True
                break

        if found:
            with open("tasks.txt", "w") as file:
                file.writelines(lines)
            print(" Task marked done.")
        else:
            print(" Task not found ")
    case 4:
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(" Error! Make sure file is in the same folder")
            lines = []
        for i, line in enumerate(lines):
            if not line.strip():
                continue
            id, task, status = line.strip().split("|")
            print(f"{id} | {task} | {status}")
        print(" Enter Task Id to remove ", end="")
        targetid = input()
        new_lines = []
        found = False
        for i, line in enumerate(lines):
            if not line.strip():
                    continue
            id, task, status = line.strip().split("|")
            if targetid.strip() == id.strip():
                found = True
                continue
            new_lines.append(line)
        if found:
            with open("tasks.txt","w") as file:
                file.writelines(new_lines)
            print(" Task removed ")
        else:
            print(" Task not found ")






