from upw.infrastructure import check_command, Command
from upw.updaters.common import UpdaterBase


class ParuUpdater(UpdaterBase):
    def __init__(self) -> None:
        super().__init__("paru", "Paru", [Command("paru -Syu")])


class YayUpdater(UpdaterBase):
    def __init__(self) -> None:
        super().__init__("yay", "Yay", [Command("yay -Syu")])


class PacmanUpdater(UpdaterBase):
    def __init__(self) -> None:
        super().__init__("pacman", "Pacman", [Command("sudo pacman -Syu")])


class ArchLinuxUpdater(UpdaterBase):
    def __init__(self) -> None:
        updaters = self.get_inner_updaters()
        super().__init__("arch_linux", "Arch Linux", None, updaters)

    @staticmethod
    def get_inner_updaters() -> list[UpdaterBase]:
        result: list[UpdaterBase] = []
        if check_command("paru"):
            result.append(ParuUpdater())
        elif check_command("yay"):
            result.append(YayUpdater())
        elif check_command("pacman"):
            result.append(PacmanUpdater())

        return result
