from upw.configuration import Updaters, AppConfiguration
from upw.updaters.archlinux import ArchLinuxUpdater
from upw.updaters.common import UpdaterBase


class OsUpdater(UpdaterBase):
    """This updater is a wrapper for all the updaters that are OS-specific."""

    def __init__(self, configuration: AppConfiguration) -> None:
        updaters = self.get_inner_updaters(configuration)
        super().__init__(Updaters.OS, configuration, None, updaters)

    @staticmethod
    def get_inner_updaters(configuration: AppConfiguration) -> list[UpdaterBase]:
        "TODO: return different updaters on different OSes."

        return [ArchLinuxUpdater(configuration)]
