from typing import Annotated

import typer

from upw import logic
from upw.configuration import AppConfiguration
from upw.logging import configure_logging


def main(
    dry_run: Annotated[bool, typer.Option()] = False,
    verbose: Annotated[bool, typer.Option()] = False,
) -> None:
    configuration = AppConfiguration(
        dry_run=dry_run,
        excluded_updaters={"paru"},
        additional_updaters=set(),
        custom_commands=set(),
        verbose=verbose,
    )
    configure_logging(configuration)
    logic.execute(configuration)


if __name__ == "__main__":
    typer.run(main)
