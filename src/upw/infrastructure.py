import shutil
import subprocess

import psutil

from upw.configuration import AppConfiguration
from upw.logging import log_info


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
        log_info(f"Running command: {command.command_str}")

        with subprocess.Popen(command.command_str, shell=True) as process:
            try:
                stdout, stderr = process.communicate()
            except:  # noqa: E722
                kill_process_and_children(process.pid)
            return_code = process.poll()

        log_info(f"Command returned: {return_code}")


def kill_process_and_children(process_id: int) -> None:
    process = psutil.Process(process_id)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()
