from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class AppConfiguration:
    dry_run: bool
    excluded_updaters: set[str]
    additional_updaters: set[str]
    custom_commands: set[str]
    verbose: bool


class Updaters(Enum):
    OS = auto()
    PARU = auto()
    YAY = auto()
    PACMAN = auto()
    ARCH = auto()


UPDATER_SPECS = {
    Updaters.OS: ("os", "Operating System", True),
    Updaters.PARU: ("paru", "Paru", False),
    Updaters.YAY: ("yay", "Yay", False),
    Updaters.PACMAN: ("pacman", "Pacman", False),
    Updaters.ARCH: ("arch", "Arch Linux", True),
}


def get_updater_id(updater: Updaters) -> str:
    return UPDATER_SPECS[updater][0]


def check_updater_not_excluded(
    updater: Updaters, configuration: AppConfiguration
) -> bool:
    return get_updater_id(updater) not in configuration.excluded_updaters
