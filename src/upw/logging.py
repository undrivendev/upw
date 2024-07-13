import logging

from upw.configuration import AppConfiguration

LOGGING_CONFIGURED = False
LOGGER = logging.getLogger("upw")


def configure_logging(configuration: AppConfiguration) -> None:
    if configuration.verbose:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.WARNING)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    LOGGER.addHandler(console_handler)

    global LOGGING_CONFIGURED
    LOGGING_CONFIGURED = True


def check_logger_configured() -> None:
    if not LOGGING_CONFIGURED:
        raise RuntimeError("Logger not configured")


def log(message: str, level: int) -> None:
    check_logger_configured()
    LOGGER.log(msg=message, level=level)


def log_debug(message: str) -> None:
    log(message, level=logging.DEBUG)


def log_info(message: str) -> None:
    log(message, level=logging.INFO)


def log_warning(message: str) -> None:
    log(message, level=logging.WARNING)


def log_error(message: str) -> None:
    log(message, level=logging.ERROR)


def log_exception(message: str) -> None:
    check_logger_configured()
    LOGGER.exception(msg=message)
