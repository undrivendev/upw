from upw.updaters.archlinux import ArchLinuxUpdater
from upw.updaters.common import UpdaterBase


class OsUpdater(UpdaterBase):
    def __init__(self) -> None:
        updaters = self.get_inner_updaters()
        super().__init__("os", "Operating System", None, updaters)

    @staticmethod
    def get_inner_updaters() -> list[UpdaterBase]:
        "TODO: return different updaters on different OSes."

        return [ArchLinuxUpdater()]
