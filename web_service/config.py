import logging.config
import pathlib

from shared.settings.config import get_settings_logging


BASE_DIR = pathlib.Path(__file__).parent


LOGGING = get_settings_logging('web_service')
logging.config.dictConfig(LOGGING)
