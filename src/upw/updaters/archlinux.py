from upw.configuration import Updaters, AppConfiguration, check_updater_not_excluded
from upw.infrastructure import check_command, Command
from upw.updaters.common import UpdaterBase


class ParuUpdater(UpdaterBase):
    def __init__(self, configuration: AppConfiguration) -> None:
        super().__init__(Updaters.PARU, configuration, [Command("paru -Syu")])


class YayUpdater(UpdaterBase):
    def __init__(self, configuration: AppConfiguration) -> None:
        super().__init__(Updaters.YAY, configuration, [Command("yay -Syu")])


class PacmanUpdater(UpdaterBase):
    def __init__(self, configuration: AppConfiguration) -> None:
        super().__init__(Updaters.PACMAN, configuration, [Command("sudo pacman -Syu")])


class ArchLinuxUpdater(UpdaterBase):
    def __init__(self, configuration: AppConfiguration) -> None:
        updaters = self.get_inner_updaters(configuration)
        super().__init__(Updaters.ARCH, configuration, None, updaters)

    @staticmethod
    def get_inner_updaters(configuration: AppConfiguration) -> list[UpdaterBase]:
        result: list[UpdaterBase] = []
        if check_command("paru") and check_updater_not_excluded(
            Updaters.PARU, configuration
        ):
            result.append(ParuUpdater(configuration))
        elif check_command("yay") and check_updater_not_excluded(
            Updaters.YAY, configuration
        ):
            result.append(YayUpdater(configuration))
        elif check_command("pacman") and check_updater_not_excluded(
            Updaters.PACMAN, configuration
        ):
            result.append(PacmanUpdater(configuration))

        return result
