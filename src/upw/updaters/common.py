from abc import ABC

from upw.configuration import AppConfiguration
from upw.infrastructure import print_message, Command, run_command


class UpdaterBase(ABC):
    def __init__(
        self,
        name: str,
        display_name: str,
        commands: list[Command] | None = None,
        inner_updaters: list["UpdaterBase"] | None = None,
    ):
        self.name = name
        self.display_name = display_name
        self.commands = commands
        self.inner_updaters = inner_updaters

    def update(self, configuration: AppConfiguration) -> None:
        print_message(f"Running {self.display_name} updater...")

        if self.commands:
            for command in self.commands:
                run_command(command, configuration)

        if self.inner_updaters:
            for updater in self.inner_updaters:
                updater.update(configuration)
