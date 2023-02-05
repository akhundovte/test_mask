import logging.config
import pathlib

from shared.settings.config import get_settings_logging


BASE_DIR = pathlib.Path(__file__).parent.parent

FILES_DIR = BASE_DIR.joinpath('files')
FILES_DIR.mkdir(exist_ok=True, parents=True)


LOGGING = get_settings_logging('loader')
logging.config.dictConfig(LOGGING)



