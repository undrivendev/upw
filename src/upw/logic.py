from upw.configuration import AppConfiguration
from upw.updaters.os import OsUpdater


def execute(configuration: AppConfiguration) -> None:
    """Execute the main update routine.

    There is a default collection of updaters that will be executed in order.
    The order is:
      - os
    """
    updaters = [OsUpdater(configuration)]

    for updater in updaters:
        updater.update()
