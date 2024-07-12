import shutil
import subprocess

from upw.configuration import AppConfiguration


def print_message(message: str) -> None:
    print(message)


def check_command(command: str) -> bool:
    return shutil.which(command) is not None


class Command:
    def __init__(self, command_str: str) -> None:
        self.command_str = command_str


def run_command(command: Command, configuration: AppConfiguration) -> None:
    if configuration.dry_run:
        print_message(f"Would run command: {command.command_str}")
    else:
        print_message(f"Running command: {command.command_str}")
        subprocess.run(command.command_str, shell=True)
