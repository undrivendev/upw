from typing import Annotated

import typer

from upw import execution
from upw.configuration import AppConfiguration


def main(dry_run: Annotated[bool, typer.Option()] = False) -> None:
    configuration = AppConfiguration(dry_run=dry_run)
    execution.execute(configuration)


if __name__ == "__main__":
    typer.run(main)
