from abc import ABC

from upw.configuration import AppConfiguration
from upw.configuration import Updaters, UPDATER_SPECS
from upw.infrastructure import print_message, Command, run_command
from upw.logging import log_info


class UpdaterBase(ABC):
    def __init__(
        self,
        updater: Updaters,
        configuration: AppConfiguration,
        commands: list[Command] | None = None,
        inner_updaters: list["UpdaterBase"] | None = None,
    ):
        self.name = UPDATER_SPECS[updater][0]
        self.display_name = UPDATER_SPECS[updater][1]
        self.skip_print_message = UPDATER_SPECS[updater][2]
        self.configuration = configuration
        self.commands = commands
        self.inner_updaters = inner_updaters

    def update(self) -> None:
        if (
            self.configuration.excluded_updaters
            and self.name in self.configuration.excluded_updaters
        ):
            log_info(f"Skipping {self.display_name} updater...")
            return

        if not self.skip_print_message:
            print_message(f"Running {self.display_name} updater...")

        if self.commands:
            for command in self.commands:
                run_command(command, self.configuration)

        if self.inner_updaters:
            for updater in self.inner_updaters:
                updater.update()
