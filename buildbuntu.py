import subprocess

sh_file_path = "cmds.sh"
with open(sh_file_path, "r") as file:
    commands = file.read().splitlines()
for command in commands:
    command = command.strip()
    subprocess.run(command.split(), check=True)
